import random
from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

#### DATA LOGIC ####
df = pd.read_csv("Day31_FlashCardApp/data/french_words.csv")
data = df.to_dict(orient="records")


def generate_new_word():
    return random.choice(data)

def set_new_word():
    new_words = generate_new_word()
    new_french = new_words["French"]
    new_english = new_words["English"]
    card_canvas.itemconfig(word_text, text=new_french)

#### UI ####
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

card_canvas = Canvas(
    width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0
)
cardfront_img = PhotoImage(file="./Day31_FlashCardApp/images/card_front.png")
card_canvas.create_image(400, 263, image=cardfront_img)
lang_text = card_canvas.create_text(
    400, 150, text="French", fill="black", font=("Ariel", 40, "italic")
)
word_text = card_canvas.create_text(
    400, 263, text="sortir", fill="black", font=("Ariel", 60, "bold")
)
card_canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="./Day31_FlashCardApp/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=set_new_word)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="./Day31_FlashCardApp/images/right.png")
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0)
right_button.grid(column=1, row=1)


window.mainloop()
