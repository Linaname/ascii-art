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
    uid = hashlib.md5(art.encode('utf-8')).hexdigest()
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
    img = Image.open(file)
    art = create_art(img, 200, (2, 2), convert_monochrome, contrast=5)
    uid = save_art(art)
    return flask.redirect(f'/{uid}')


@app.route('/<art_id>', methods=['GET'])
def output(art_id):
    art = load_art(art_id)
    return render_template('output.html', art=art)


if __name__ == '__main__':
    os.makedirs(SAVED_ARTS_DIR, exist_ok=True)
    port = int(os.environ.get('PORT', '5000'))
    app.run(host='0.0.0.0', port=port)
