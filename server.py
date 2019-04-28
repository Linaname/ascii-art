from flask import Flask, request, render_template
from main import create_art, convert_monochrome
from PIL import Image
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    print(request.method)
    if request.method == 'POST':
        file = request.files['file']
        img = Image.open(file)
        art = create_art(img, 200, (2, 2), convert_monochrome, brightness=0.9)
        lines = art.splitlines()
        return render_template('output.html', art=art)
    return render_template('main.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '5000'))
    app.run(host='0.0.0.0', port=port)
