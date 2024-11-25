class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_anwser(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_number + 1}\n")

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        user_answer = input(
            f"Q. {self.question_number + 1}: {self.question_list[self.question_number].text} (True/False): "
        )
        self.check_anwser(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1
