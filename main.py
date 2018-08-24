from PIL import Image
from PIL import ImageEnhance
import sys

MONOCHROME_CONVERTING_MODES = {
    '1x1': {
        'size': (1, 1),
        'chars': {
            ((0,),): ' ',
            ((1,),): '❀',
        },
    },
    '1x2': {
        'size': (1, 2),
        'chars': {
            ((0,),
             (0,),): ' ',
            ((0,),
             (1,),): '▄',
            ((1,),
             (0,),): '▀',
            ((1,),
             (1,),): '█',
        },
    },
    '2x2': {
        'size': (2, 2),
        'chars': {
            ((0, 0),
             (0, 0),): ' ',
            ((0, 0),
             (0, 1),): '▗',
            ((0, 0),
             (1, 0),): '▖',
            ((0, 0),
             (1, 1),): '▄',
            ((0, 1),
             (0, 0),): '▝',
            ((0, 1),
             (0, 1),): '▐',
            ((0, 1),
             (1, 0),): '▞',
            ((0, 1),
             (1, 1),): '▟',
            ((1, 0),
             (0, 0),): '▘',
            ((1, 0),
             (0, 1),): '▚',
            ((1, 0),
             (1, 0),): '▌',
            ((1, 0),
             (1, 1),): '▙',
            ((1, 1),
             (0, 0),): '▀',
            ((1, 1),
             (0, 1),): '▜',
            ((1, 1),
             (1, 0),): '▛',
            ((1, 1),
             (1, 1),): '█',
        },
    },
}


def prepare_image(image, ascii_width, block_size, contrast=5.0):
    prepared_image = image.convert('L')
    image_width, image_height = image.size
    block_width, block_height = block_size
    ascii_height = image_height * ascii_width // (2 * image_width)
    enh = ImageEnhance.Contrast(prepared_image)
    prepared_image = enh.enhance(contrast)
    prepared_image = prepared_image.resize((ascii_width*block_width,
                                            ascii_height*block_height))
    return prepared_image, ascii_height


def get_block(pixels, ascii_position, block_size):
    block_width, block_height = block_size
    ascii_x, ascii_y = ascii_position
    pixels_block = tuple(tuple(pixels[image_x, image_y] for image_x in
                               range(ascii_x * block_width,
                                     (ascii_x + 1) * block_width)) for image_y
                         in range(ascii_y * block_height,
                                  (ascii_y + 1) * block_height))
    return pixels_block


def is_black(pixel):
    return pixel > 200


def convert_pixels_to_char(pixels_block, mode): 
    return MONOCHROME_CONVERTING_MODES[mode]['chars'][pixels_block]


path = sys.argv[1]
image = Image.open(path)
ascii_width = int(sys.argv[2])
mode = sys.argv[3]
block_size = MONOCHROME_CONVERTING_MODES[mode]['size']
block_width, block_height = block_size
prepared_image, ascii_height = prepare_image(image, ascii_width, block_size, 2)
pixels = prepared_image.point(is_black).load()
for ascii_y in range(ascii_height):
    ascii_line = []
    for ascii_x in range(ascii_width):
        pixels_block = get_block(pixels, (ascii_x, ascii_y,), block_size)
        ascii_line.append(convert_pixels_to_char(pixels_block, mode))
    print(*ascii_line, sep='')
