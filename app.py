import os
from flask import Flask, after_this_request, render_template, request, flash, redirect, send_from_directory
from werkzeug.utils import secure_filename
import subprocess

UPLOAD_FOLDER = './upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_for_save = app.config['UPLOAD_FOLDER']+"/"+filename
            exiftool_command = ["exiftool", "-all=", "-overwrite_original", file_for_save, file_for_save]
            subprocess.run(exiftool_command)
            return download_file(filename)
    return render_template('index.html')

@app.route('/download/<name>')
def download_file(filename):
    @after_this_request
    def remove_file(response):
        try:
            os.remove(app.config['UPLOAD_FOLDER']+"/"+filename)
        except Exception as error:
            app.logger.error("Error removing or closing downloaded file handle", error)
        return response
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)