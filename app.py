import os
import sys
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


@app.route('/tests', methods=['GET', 'POST'])
def get_test_list_page():
    return render_template('tests.html')


@app.route('/test', methods=['GET', 'POST'])
def get_test_page():
    test: tests.Test = tests.TestManager.test_from_json("test.json")
    a = request
    return a.form

    options = []

    for q in test.questions:
        for o in q.options:
            options.append(str(o))
        break
    return render_template('yea.html', questions=options)


@app.route('/about', methods=['GET', 'POST'])
def get_test_about_page():
    test: tests.Test = tests.TestManager.test_from_json("test.json")
    return render_template('about_test.html')


@app.route('/main', methods=['GET', 'POST'])
def get_main_page():
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



def main():
    app.run()


if __name__ == '__main__':
    main()

