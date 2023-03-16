import os
import threading

from flask import Flask, request, url_for, render_template
from werkzeug.utils import secure_filename, redirect

import gui
import tests
import util
from util import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('main.html')


@app.route('/decrypt', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(f"./files/{filename}")
            return JsonManager.decrypt(JsonManager.read(f"./files/{filename}"))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/test', methods=['GET', 'POST'])
def get_test_page():
    return render_template('index.html')


def main():
    app.run()


if __name__ == '__main__':
    main()

