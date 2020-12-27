import os

from flask import render_template
from flask import request, redirect, url_for
from flask import send_file
from werkzeug.utils import secure_filename

from filter_app.commands.FaceDetectCommand import FaceDetectCommand
from filter_app.commands.black_white_command import BlackAndWhiteCommand
from filter_app.commands.brightness_command import BrightnessCommand
from filter_app.commands.contrast_command import ContrastCommand
from filter_app.commands.negative_command import NegativeCommand
from filter_app.commands.rotate_command import RotateCommand
from filter_app.commands.sepia_command import SepiaCommand
from flask_app.app import app
from flask_app.config import ALLOWED_EXTENSIONS
from flask_app.utils.apply_command import apply_commands

COMMANDS = {"FaceDetectCommand": FaceDetectCommand,
            "BlackWhite": BlackAndWhiteCommand,
            "Brightness": BrightnessCommand,
            "Sepia": SepiaCommand,
            "Contrast": ContrastCommand,
            "Negative": NegativeCommand,
            "rotate_90": RotateCommand,
            }

PATH = "static/"


commands_history = []
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
            commands_history.append(tuple(["Start", filename]))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

    return render_template("index.html")


@app.route('/choose_filter/<filename>')
def uploaded_file(filename):
    return render_template("filter_type.html", filename=filename, commands_history=commands_history)


@app.route('/choose_filter/face_detect/<filename>')
def face_detect_view(filename):
    return render_template("filter_choose_1.html", filename=filename, commands_history=commands_history)


@app.route('/choose_filter/color/<filename>')
def color_view(filename):
    return render_template("filter_choose_3.html", filename=filename)


@app.route('/choose_filter/rotate/<filename>')
def rotate_view(filename):
    return render_template("filter_choose_2.html", filename=filename, commands_history=commands_history)


@app.route('/choose_filter/face_detect/apply/<command>/<filename>')
def apply_command(command, filename):
    new_filename = apply_commands(COMMANDS[command], filename)
    commands_history.append(tuple([COMMANDS[command].apply_name, new_filename]))
    return redirect(url_for('uploaded_file', filename=new_filename))


@app.route('/get_image/<filename>')
def get_image(filename):
    return send_file(PATH+filename, mimetype='image/gif')


@app.route('/undo_command/')
def undo():
    try:
        commands_history.pop()
        filename = commands_history[-1][1]
        return redirect(url_for('uploaded_file', filename=filename))
    except IndexError:
        return redirect(url_for('upload_file'))
