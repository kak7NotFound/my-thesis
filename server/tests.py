import datetime
from util import *


class TestManager:
    def import_manually(self):
        return

    def export_manually(self):
        return

    def import_from_server(self):
        return

    def export_to_server(self):
        return


class Test:

    # todo PERMISSIONS?

    def __init__(self):
        test_id: int
        test_type: TestType
        author: str
        createdAt: datetime.datetime

        passingScore: int
        attempts: int
        timeLimitSecs: int

        questions: list[Question] = list()


class Question:
    def __init__(self):
        question_type: QuestionType
        questions: list
        answer = None


