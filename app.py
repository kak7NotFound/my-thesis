from flask import Flask, request, render_template, session, jsonify
from flask_cors import CORS, cross_origin
from flask_session import Session
from werkzeug.utils import secure_filename

import tests
from util import *


app = Flask(__name__, static_folder="templates")
app.static_folder = 'templates'
app.secret_key = '04d7b317de955beea1f17536282b121a1b88b61cbe23e56855fdabb4bd70ecd0c39f851c16b7124b53e75daa2625781e80f48ecdb5f1be58859aa78c4808bc30'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_FILE_DIR'] = r'sessions'
app.config.from_object(__name__)
Session(app)
CORS(app, resources={r"*": {"origins": "*"}}, supports_credentials=True)


IS_OFFLINE = False

database = DataBase()


# todo remove db add database()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
@cross_origin(supports_credentials=True)
def login():

    data = request.get_json()

    collection = database.db['users']['users']
    result = collection.find_one({
        'login': data['login'],
        'password': data['password']
    })
    print(result)
    if result is not None:
        session['user_id'] = result['id']
        print("РЕЗУЛЬТАТ СЕССИИ ЗАПИСАН", session['user_id'])
        for key, value in session.items():
            print(f'session: {key} = {value}')
        return jsonify(result['id'])
    else:
        return jsonify("None")


@app.route('/get_session_data', methods=['GET'])
def get_session_data():
    session_data = session.get('user_id', '')
    return jsonify(session_data)


@app.route('/tests', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def get_test_list_html():

    # todo remove abs path
    print("got user id " + str(session.get('user_id')))

    # print("GET SESSION DATA " + session)
    # return redirect("tests.html")
    test_template = open(r"C:\Users\kak7\Documents\GitHub\my-thesis\templates\test.html", "r", encoding="utf-8").read()

    html = ""

    for test in tests.TestManager.get_all_test_as_dict():
        test: tests.Test
        # todo доделать хуйню
        html = html + test_template.replace("{title}", test.title).replace("{author}", test.author).replace(
            "{test_type}", "тип теста дааа").replace("{test_id}", str(test.test_id))
    for key, value in session.items():
        print(f'session: {key} = {value}')
    return html


@app.route('/save_test', methods=['post'])
def save_test():
    print(request.get_json())
    return jsonify("success")

@app.route('/test', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
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
    test_id = request.form.get('button_id')
    return render_template('about_test.html')
    # return open(r"C:\Users\kak7\Documents\GitHub\my-thesis\templates\about_test.html", "r", encoding="utf-8").read()


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
    app.run(threaded=False)


if __name__ == '__main__':
    main()

    # local_db_thread.terminate()
