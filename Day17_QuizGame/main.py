from question_model import Question
from data import question_data

question_bank = []

for dict in question_data:
    question_bank.append(Question(dict["text"], dict["answer"]))

