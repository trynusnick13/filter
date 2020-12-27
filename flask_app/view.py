import os

from flask import request, redirect, url_for
from flask import render_template
from werkzeug.utils import secure_filename

from flask_app.app import app
from flask_app.config import ALLOWED_EXTENSIONS
from filter_app.commands.FaceDetectCommand import FaceDetectCommand
from filter_app.image.base_image import Image
import PIL
import datetime

current_file = []


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            current_file.append(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

    return render_template("index.html")


@app.route('/choose_filter/<filename>')
def uploaded_file(filename):
    return render_template("filter_type.html", filename=filename)


@app.route('/choose_filter/face_detect/<filename>')
def face_detect_view(filename):
    return render_template("filter_choose_1.html", filename=filename)


@app.route('/choose_filter/face_detect/apply/<filename>')
def apply_face_detect(filename):
    pil_image = PIL.Image.open(f'./static/{filename}')
    base_image = Image("temp-name", pil_image)
    a = FaceDetectCommand(base_image)
    new_file = a.execute()
    timestamp_now = datetime.datetime.now()
    path = "./static/"
    new_file.name = f"{timestamp_now.timestamp()}-{filename}"
    new_file.save_file(name=path+new_file.name)
    return redirect(url_for('uploaded_file', filename=new_file.name))


if __name__ == '__main__':
    filename = "aaa4.png"
    timestamp_now = datetime.datetime.now()
    pil_image = PIL.Image.open(f'./static/{filename}')
    base_image = Image("jacky chan", pil_image)
    a = FaceDetectCommand(base_image)
    new_file = a.execute()
    new_file.name = f"./static/{timestamp_now.timestamp()}-{filename}"
    new_file.save_file(name=new_file.name)

    # PIL.Image._show(a.execute().pillow_image)


