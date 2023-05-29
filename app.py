from flask import Flask, request, render_template, session, jsonify, redirect
from flask_cors import CORS
from werkzeug.utils import secure_filename

import tests
from util import *

app = Flask(__name__, static_folder="templates")
app.static_folder = 'templates'
app.secret_key = 'your-secret-key'
cors = CORS(app, resources={r"*": {"origins": "*"}}, supports_credentials=True)

IS_OFFLINE = False

database = DataBase()


# todo remove db add database()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    collection = database.db['users']['users']
    result = collection.find_one({
        'login': data['login'],
        'password': data['password']
    })
    print(result)
    if result is not None:
        return jsonify(result['id'])
    else:
        return jsonify("None")


@app.route('/get_session_data', methods=['GET'])
def get_session_data():
    session_data = session.get('user_id', '')
    return jsonify(session_data)


@app.route('/set_session_data', methods=['POST'])
def set_session_data():
    data = request.get_json()
    print(data)
    session['user_id'] = data['user_id']
    return jsonify({'message': 'Session value set successfully'})


@app.route('/tests', methods=['GET', 'POST'])
def get_test_list_html():
    # todo remove abs path

    # print("GET SESSION DATA " + session)
    return redirect("tests.html")
    test_template = open(r"C:\Users\kak7\Documents\GitHub\my-thesis\templates\test.html", "r", encoding="utf-8").read()

    html = ""

    for test in tests.TestManager.get_all_test_as_dict():
        test: tests.Test
        # todo доделать хуйню
        html = html + test_template.replace("{title}", test.title).replace("{author}", test.author).replace(
            "{test_type}", "тип теста дааа").replace("{test_id}", str(test.test_id))

    return html


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
