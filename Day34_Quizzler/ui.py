from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(
            text="Score: 0",
            font=("Arial", 10, "normal"),
            background=THEME_COLOR,
            fg="white",
        )
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, font=("Arial", 20, "italic"), fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="Day34_Quizzler/images/true.png")
        self.true_button = Button(
            image=true_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.anwser_button_pressed("true"),
        )
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="Day34_Quizzler/images/false.png")
        self.false_button = Button(
            image=false_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.anwser_button_pressed("false"),
        )
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def anwser_button_pressed(self, answer):
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
