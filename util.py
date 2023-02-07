import base64
from enum import Enum


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
