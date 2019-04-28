from flask import Flask, request, render_template
from main import create_art, convert_monochrome
from PIL import Image

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    print(request.method)
    if request.method == 'POST':
        file = request.files['file']
        img = Image.open(file)
        art = create_art(img, 80, (2, 2), convert_monochrome, brightness=0.9)
        lines = art.splitlines()
        return render_template('output.html', lines=lines)
    return render_template('main.html')


if __name__ == '__main__':
    app.run()