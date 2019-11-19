from flask import Flask, send_file
from PIL import Image, ImageDraw
import io

app = Flask(__name__)


def send_pil_image(img):
    img_io = io.BytesIO()
    img.save(img_io, 'png')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


@app.route('/<int:width>x<int:height>')
def placeholder(width, height):
    img = Image.new('RGB', (width, height), color=(200, 200, 200))
    draw = ImageDraw.Draw(img)

    msg = f"{width}x{height}"
    w, h = draw.textsize(msg)
    position = (width - w) / 2, (height - h) / 2
    draw.text(position, msg, fill="black")

    return send_pil_image(img)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
