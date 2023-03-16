import tests

TEST = tests.TestManager.test_from_json("test.json")

print(TEST.questions)