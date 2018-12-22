# ascii-art
Скрипт для создания **теперь цветного!** отображаемого в консоли ASCII-арта из несложного изображения

# Usage
```
usage: main.py [-h] [--width WIDTH] [--block BLOCK] [--mode MODE] path

positional arguments:
  path           path to image

optional arguments:
  -h, --help     show this help message and exit
  --width WIDTH  art width (default: current terminal width)
  --block BLOCK  size of pixel block converted to single char.
                 Available: 'x1'(default), '1x2'
  --mode MODE    color depth (bits) used in art. Available: '3', '3/4', '4',
                 '24'
```
