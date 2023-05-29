import datetime
import json

import app
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
    def test_from_json(json_dict: dict):
        # data: dict = json.loads(json_str)
        data = json_dict
        return Test(data.get("test_id"), data.get("title"), data.get("test_type"), data.get("author"), data.get("created_at"),
                    data.get("passingScore"), data.get("attempts"), data.get("timeLimitSecs"), data.get("questions"))

    @staticmethod
    def get_all_test_as_dict():
        tests = []
        for test in app.database.db["tests"]["tests"].find():
            tests.append(TestManager.test_from_json(test))
        return tests


class Test:

    # todo PERMISSIONS?

    def __init__(self, test_id, title, test_type, author, created_at, passingScore, attempts, timeLimitSecs, questions_as_list):
        self.test_id: int = test_id
        self.title: str = title
        self.test_type: TestType = test_type
        self.author: str = author
        self.createdAt: datetime.datetime = created_at

        self.passingScore: int = passingScore
        self.attempts: int = attempts
        self.timeLimitSecs: int = timeLimitSecs

        self.questions: list[Question] = list()
        for q in questions_as_list:
            q: dict
            # print(q)
            self.questions.append(Question(QuestionType[q.get("type")], q.get("question").get("text"), q.get("question").get("options"), q.get("question").get("answer")))


class Question:
    def __init__(self, question_type, text, options, answer=None):
        # print(question_type, text, options, answer)
        self.question_type: QuestionType = question_type
        self.text: str = text
        self.options: list = options
        self.answer: str = answer

