import datetime
import json

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

    def get_test_by_id(self):
        return

    @staticmethod
    def test_from_json(file_name: str):
        data: dict = json.loads(open(file_name, "r", encoding="utf-8").read())
        return Test(data.get("test_id"), data.get("test_type"), data.get("author"), data.get("created_at"),
                    data.get("passingScore"), data.get("attempts"), data.get("timeLimitSecs"), data.get("questions"))


class Test:

    # todo PERMISSIONS?

    def __init__(self, test_id, test_type, author, created_at, passingScore, attempts, timeLimitSecs, questions_as_list):
        self.test_id: int = test_id
        self.test_type: TestType = test_type
        self.author: str = author
        self.createdAt: datetime.datetime = created_at

        self.passingScore: int = passingScore
        self.attempts: int = attempts
        self.timeLimitSecs: int = timeLimitSecs

        self.questions: list[Question] = list()

        for q in questions_as_list:
            q: dict
            self.questions.append(Question(QuestionType[q.get("type")], q.get("text"), q.get("options"), q.get("answer")))


class Question:
    def __init__(self, question_type, text, options, answer=None):
        print(question_type)
        self.question_type: QuestionType = question_type
        self.text: str = text
        self.options: list = options
        self.answer: str = answer

