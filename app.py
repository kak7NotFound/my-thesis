import subprocess
import threading

import pymongo
from flask import Flask, request, render_template
from flask_cors import CORS
from pymongo import MongoClient
from werkzeug.utils import secure_filename

import tests
from util import *

app = Flask(__name__)
cors = CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": ["*"],
        "methods": ["GET", "POST"]
    }
})

IS_OFFLINE = False
db = None
do_stop = threading.Event()
local_db_thread = None


def start_local_db():
    # todo уменьшить задерку, там что-то не работает
    mongo_process = subprocess.Popen(r"C:\Users\kak7\Documents\GitHub\my-thesis\mongo\start.bat")
    local_db_thread = mongo_process


def create_local_copy_then_close():
    thread = threading.Thread(target=start_local_db)
    thread.start()
    local_db = MongoClient('mongodb://127.0.0.1:27026', connect=True, serverSelectionTimeoutMS=500)

    local_db_thread.terminate()


try:
    maindb = MongoClient('mongodb://127.0.0.1:27017', connect=True, serverSelectionTimeoutMS=500)
    maindb.server_info()
    db = maindb
except pymongo.errors.ConnectionFailure:
    IS_OFFLINE = True
    thread = threading.Thread(target=start_local_db)
    thread.start()


db = MongoClient('mongodb://127.0.0.1:27026', connect=True, serverSelectionTimeoutMS=500)
print("OFFLINE MODE: ", IS_OFFLINE)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tests', methods=['GET', 'POST'])
def get_test_list_page():
    # todo remove abs path
    test_template = open(r"C:\Users\kak7\Documents\GitHub\my-thesis\templates\test.html", "r", encoding="utf-8").read()
    return test_template


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
    local_db_thread.terminate()
