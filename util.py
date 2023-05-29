import base64
import subprocess
import threading
from enum import Enum

import pymongo
from pymongo import MongoClient


class Account:
    pass


class TestType(Enum):
    EDUCATION = 1,
    ATTESTATION = 2


class QuestionType(Enum):
    SINGLE = 1,
    MULTIPLY = 2,
    MATCHING = 3,
    ORDER = 4


class AccountType(Enum):
    STUDENT = 1,
    DON = 2,
    ADMIN = 3


class JsonManager:

    @staticmethod
    def test():
        json = JsonManager.read("crypted_test.test")

        return json

    @staticmethod
    def read(file_name):
        jsonFile = open(file_name, "r", encoding="UTF-8")
        # d = json.loads(jsonFile.read())
        return jsonFile.read()

    @staticmethod
    def encrypt(text):
        b = base64.b64encode(bytes(text, 'utf-8'))
        base64_str = b.decode('utf-8')
        return str(base64_str)

    @staticmethod
    def decrypt(b64):
        return base64.b64decode(b64).decode()

    @staticmethod
    def save_encrypted_text(location: str):
        return


class DataBase:

    db = None
    do_stop = threading.Event()
    local_db_thread = None

    def __init__(self):
        db = MongoClient('mongodb://127.0.0.1:27026', connect=True, serverSelectionTimeoutMS=500)

    def start_local_db():
        mongo_process = subprocess.Popen(r"C:\Users\kak7\Documents\GitHub\my-thesis\mongo\start.bat")
        local_db_thread = mongo_process

    # TODO LOCAL MODE (OFFLINE)
    def create_local_copy_then_close():
        thread = threading.Thread(target=start_local_db)
        thread.start()
        local_db = MongoClient('mongodb://127.0.0.1:27026', connect=True, serverSelectionTimeoutMS=500)

        # todo copy
        # https://www.mongodb.com/docs/database-tools/

        local_db.close()
        local_db_thread.terminate()

    try:
        maindb = MongoClient('mongodb://127.0.0.1:27017', connect=True, serverSelectionTimeoutMS=500)
        maindb.server_info()
        db = maindb
    except pymongo.errors.ConnectionFailure:
        IS_OFFLINE = True
        thread = threading.Thread(target=start_local_db)
        thread.start()
        db = MongoClient('mongodb://127.0.0.1:27026', connect=True, serverSelectionTimeoutMS=800)

    # print("OFFLINE MODE: ", IS_OFFLINE)
