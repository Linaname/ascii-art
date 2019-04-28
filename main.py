from PIL import Image, ImageEnhance, ImageOps
import os, argparse
import constants
from constants import NBSP


def prepare_image(initial_image, ascii_width, block_size, contrast=1, brightness=1, reverse=False):
    image = initial_image.convert('RGB')
    if reverse:
        image = ImageOps.invert(image)
    image = ImageEnhance.Brightness(image).enhance(brightness)
    image = ImageEnhance.Contrast(image).enhance(contrast)
    image_width, image_height = image.size
    block_width, block_height = block_size
    ascii_height = image_height * ascii_width // (2 * image_width)
    resized_image = image.resize((ascii_width*block_width, ascii_height*block_height))
    pixels = resized_image.load()
    prepared_image = [[get_block(pixels, (x, y), block_size) for x in range(ascii_width)] for y in range(ascii_height)]
    return prepared_image


def get_block(pixels, ascii_position, block_size):
    block_width, block_height = block_size
    ascii_x, ascii_y = ascii_position
    x_interval = range(ascii_x * block_width, (ascii_x + 1) * block_width)
    y_interval = range(ascii_y * block_height, (ascii_y + 1) * block_height)
    pixel_block = tuple(tuple(pixels[x, y][:3] for x in x_interval) for y in y_interval)
    return pixel_block


def color_distance(point1, point2):
    r1, g1, b1 = point1
    r2, g2, b2 = point2
    return abs(r1 - r2)**2 + abs(g1 - g2)**2 + abs(b1 - b2)**2


def find_best_color(point, color_map):
    code = min(color_map, key=lambda code: color_distance(point, color_map[code]))
    return code


def convert_for_tty(pixel_block):
    block_size = (len(pixel_block[0]), len(pixel_block))
    if block_size == (1, 2):
        return convert_3_bit(pixel_block)
    elif block_size == (1, 1):
        return convert_4_bit(pixel_block)


def convert_3_bit(pixel_block, r_threshold=128, g_threshold=128, b_threshold=128):
    block_size = (len(pixel_block[0]), len(pixel_block))
    if block_size == (1, 2):
        top = pixel_block[0][0]
        r, g, b = top
        top_color = 40 + (r >= r_threshold)*1 + (g >= g_threshold)*2 + (b >= b_threshold)*4
        bottom = pixel_block[1][0]
        r, g, b = bottom
        bottom_color = 30 + (r >= r_threshold)*1 + (g >= g_threshold)*2 + (b >= b_threshold)*4
        return f'\033[0;{bottom_color};{top_color}m▄\033[0m'
    elif block_size == (1, 1):
        bottom = pixel_block[0][0]
        r, g, b = bottom
        bottom_color = 40 + (r >= r_threshold) * 1 + (g >= g_threshold) * 2 + (b >= b_threshold) * 4
        return f'\033[0;{bottom_color}m{NBSP}\033[0m'


def convert_4_bit(pixel_block):
    block_size = (len(pixel_block[0]), len(pixel_block))
    if block_size == (1, 2):
        top = pixel_block[0][0]
        top_code = find_best_color(top, constants.vga_4_bit_color_map) + 10
        bottom = pixel_block[1][0]
        bottom_code = find_best_color(bottom, constants.vga_4_bit_color_map)
        return f'\033[0;{bottom_code};{top_code}m▄\033[0m'
    elif block_size == (1, 1):
        point = pixel_block[0][0]
        code = find_best_color(point, constants.vga_4_bit_color_map)
        return f'\033[0;{code}m█\033[0m'


def convert_24_bit(pixel_block):
    block_size = (len(pixel_block[0]), len(pixel_block))
    if block_size == (1, 2):
        top = pixel_block[0][0]
        r, g, b = top
        top_color = f'\033[48;2;{r};{g};{b}m'
        bottom = pixel_block[1][0]
        r, g, b = bottom
        bottom_color = f'\033[38;2;{r};{g};{b}m'
        return f'{top_color}{bottom_color}▄\033[00m'
    elif block_size == (1, 1):
        bottom = pixel_block[0][0]
        r, g, b = map(lambda x: int((x/255)**1*255), bottom)
        bottom_color = f'\033[48;2;{r};{g};{b}m'
        return f'\033[1m{bottom_color}{NBSP}\033[00m'


def create_art(image, ascii_width, block_size, convert_method, **kwargs):
    prepared_image = prepare_image(image, ascii_width, block_size, **kwargs)
    ascii_height = len(prepared_image)
    lines = []
    for ascii_y in range(ascii_height):
        ascii_line = []
        for ascii_x in range(ascii_width):
            pixel_block = prepared_image[ascii_y][ascii_x]
            ascii_line.append(convert_method(pixel_block))
        lines.append(''.join(ascii_line))
    return '\n'.join(lines)


def convert_monochrome(pixel_block, threshold=128):
    pixel_block = to_mono(pixel_block, threshold=threshold)
    block_size = len(pixel_block[0]), len(pixel_block)
    return constants.block_symbols[block_size][pixel_block]


def parse_resolution(arg):
    return tuple(map(int, arg.split('x')))


def to_mono(pixel_block, threshold=128):
    return tuple(tuple(int((r+g+b)//3<=threshold) for r, g, b in row) for row in pixel_block)


if __name__ == '__main__':
    method_map = {
        '3': convert_3_bit,
        '3/4': convert_for_tty,
        '4': convert_4_bit,
        '24': convert_24_bit,
        '1': convert_monochrome,
    }
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                        type=str,
                        help='path to image',
                        )
    parser.add_argument('--width',
                        type=int,
                        help='art width (default: current terminal width)',
                        )
    parser.add_argument('--block',
                        type=parse_resolution,
                        help="size of pixel block converted to single char. Available:\u00A0'1x1'(default),\u00A0'1x2'",
                        default='1x1',
                        )
    parser.add_argument('--mode',
                        type=str,
                        help="color depth (bits) used in art. Available: '1' (monochrome), '3', '3/4', '4', '24'",
                        default='3/4',
                        )
    parser.add_argument('--contrast',
                        type=float,
                        help="change contrast of image. Default: 1",
                        default=1,
                        )
    parser.add_argument('--brightness',
                        type=float,
                        help="change brightness of image. Default: 1",
                        default=1,
                        )
    parser.add_argument('-r', '--reverse',
                        help='reverse colors of image',
                        action='store_true',
                        )
    args = parser.parse_args()
    path = args.path
    ascii_width = args.width or os.get_terminal_size().columns
    image = Image.open(path)
    contrast = args.contrast
    block_size = args.block
    convert_method = method_map[args.mode]
    art = create_art(image, ascii_width, block_size, convert_method,
                     contrast=args.contrast,
                     brightness=args.brightness,
                     reverse=args.reverse)
    print(art)
