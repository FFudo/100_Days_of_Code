from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", font=("Arial", 10, "normal"), background=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.canvas.create_text(
            150, 125, text="Some Question", font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2)

        true_img = PhotoImage(file="Day34_Quizzler/images/true.png")
        self.true_button = Button(image=true_img, borderwidth=0, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="Day34_Quizzler/images/false.png")
        self.false_button = Button(image=false_img, borderwidth=0, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()
