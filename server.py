from flask import Flask, request, render_template
import flask
from main import create_art, convert_monochrome
from PIL import Image
import os
import hashlib

SAVED_ARTS_DIR = 'arts'

app = Flask(__name__)


def get_file_path(uid):
    return os.path.join(SAVED_ARTS_DIR, str(uid))


def create_art_uid(art):
    uid = hashlib.md5(art.encode('utf-8')).hexdigest()[:8]
    return uid


def save_art(art, uid=None):
    if uid is None:
        uid = create_art_uid(art)
    with open(get_file_path(uid), 'w') as f:
        f.write(art)
    return uid


def load_art(uid):
    filepath = get_file_path(uid)
    with open(filepath, 'r') as f:
        art = f.read()
    return art


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('main.html')
    file = request.files['file']
    contrast = int(request.form.get('contrast', '100'))/100
    brightness = int(request.form.get('brightness', '100'))/100
    width = int(request.form.get('width', '200'))
    block = request.form.get('block')
    block_size = tuple(map(int, block.split('x')))
    dithering = 'dithering' in request.form
    mode = '1' if dithering else 'RGB'
    img = Image.open(file)
    params = {
        'contrast': contrast,
        'brightness': brightness,
        'mode': mode,
    }
    art = create_art(img, width, block_size, convert_monochrome, **params)
    uid = save_art(art)
    return flask.redirect(f'/{uid}')


@app.route('/<art_id>', methods=['GET'])
def output(art_id):
    try:
        art = load_art(art_id)
    except FileNotFoundError:
        flask.abort(404)
    return render_template('output.html', art=art)


if __name__ == '__main__':
    os.makedirs(SAVED_ARTS_DIR, exist_ok=True)
    port = int(os.environ.get('PORT', '5000'))
    app.run(host='0.0.0.0', port=port)
