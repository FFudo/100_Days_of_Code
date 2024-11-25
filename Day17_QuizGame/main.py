from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for dict in question_data:
    question_bank.append(Question(dict["text"], dict["answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score was: {quiz.score}/{quiz.question_number}")