import os

from flask import Flask, request, url_for
from werkzeug.utils import secure_filename, redirect

import util
from util import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return util.JsonManager.test()


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
