from PIL import Image
import sys, os, argparse
import constants


def prepare_image(image, ascii_width, block_size):
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
    pixel_block = [[pixels[x, y][:3] for x in x_interval] for y in y_interval]
    return pixel_block


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
        return f'\033[1m{bottom_color} \033[00m'


def color_distance(point1, point2):
    r1, g1, b1 = point1
    r2, g2, b2 = point2
    return abs(r1 - r2)**2 + abs(g1 - g2)**2 + abs(b1 - b2)**2


def find_best_color(point, color_map):
    code = min(color_map, key=lambda code: color_distance(point, color_map[code]))
    return code


def convert_for_fucking_tty(pixel_block):
    block_size = (len(pixel_block[0]), len(pixel_block))
    if block_size == (1, 2):
        top = pixel_block[0][0]
        top_code = find_best_color(top, constants.vga_color_map) + 10
        bottom = pixel_block[1][0]
        bottom_code = find_best_color(bottom, constants.vga_color_map)
        return f'\033[0;{bottom_code};{top_code}m▄\033[0m'
    elif block_size == (1, 1):
        point = pixel_block[0][0]
        code = find_best_color(point, constants.vga_advanced_color_map)
        return f'\033[0;{code}m█\033[0m'


def convert_3_bit(pixel_block, r_threshold=128, g_threshold=128, b_threshold=128):
    block_size = (len(pixel_block[0]), len(pixel_block))
    if block_size == (1, 2):
        top = pixel_block[0][0]
        r, g, b = top
        top_color = 40 + (r >= r_threshold)*1 + (g >= g_threshold)*2 + (b >= b_threshold)*4
        bottom = pixel_block[1][0]
        r, g, b = bottom
        bottom_color = 30 + (r >= r_threshold)*1 + (g >= g_threshold)*2 + (b >= b_threshold)*4
        return f'\033[4;{bottom_color};{top_color}m▄\033[0m'
    elif block_size == (1, 1):
        bottom = pixel_block[0][0]
        r, g, b = bottom
        bottom_color = 40 + (r >= r_threshold) * 1 + (g >= g_threshold) * 2 + (b >= b_threshold) * 4
        return f'\033[0;{bottom_color}m \033[0m'


def create_art(image, ascii_width, block_size, convert_method):
    prepared_image = prepare_image(image, ascii_width, block_size)
    ascii_height = len(prepared_image)
    lines = []
    for ascii_y in range(ascii_height):
        ascii_line = []
        for ascii_x in range(ascii_width):
            pixel_block = prepared_image[ascii_y][ascii_x]
            ascii_line.append(convert_method(pixel_block))
        lines.append(''.join(ascii_line))
    return '\n'.join(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to image')
    parser.add_argument('--width', type=int, help='art width (default: current terminal width)')
    args = parser.parse_args()
    path = args.path
    ascii_width = args.width or os.get_terminal_size().columns
    image = Image.open(path)
    block_size = (1, 1)
    convert_method = convert_for_fucking_tty
    art = create_art(image, ascii_width, block_size, convert_method)
    print(art)
