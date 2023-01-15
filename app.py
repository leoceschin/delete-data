import os
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory, send_file
from werkzeug.utils import secure_filename
from exiftool import ExifTool
import subprocess

UPLOAD_FOLDER = './upload'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            exiftool_command = ["exiftool", "-all=", app.config['UPLOAD_FOLDER']+"/"+filename, app.config['UPLOAD_FOLDER']+"/"+filename]
            subprocess.run(exiftool_command)
            
            return download_page(filename)
    return render_template('index.html')

@app.route('/download/<name>')
def download_page(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)