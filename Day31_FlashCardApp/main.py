import random
from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

#### DATA LOGIC ####
df = pd.read_csv("Day31_FlashCardApp/data/french_words.csv")
to_learn = df.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    card_canvas.itemconfig(lang_label, text="French")
    french_word = current_card["French"]
    new_english = current_card["English"]
    card_canvas.itemconfig(word_label, text=french_word)


#### UI ####
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

card_canvas = Canvas(
    width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0
)
cardfront_img = PhotoImage(file="./Day31_FlashCardApp/images/card_front.png")
card_canvas.create_image(400, 263, image=cardfront_img)
lang_label = card_canvas.create_text(
    400, 150, text="Title", fill="black", font=("Ariel", 40, "italic")
)
word_label = card_canvas.create_text(
    400, 263, text="Word", fill="black", font=("Ariel", 60, "bold")
)
card_canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="./Day31_FlashCardApp/images/wrong.png")
wrong_button = Button(
    image=wrong_img, highlightthickness=0, borderwidth=0, command=next_card
)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="./Day31_FlashCardApp/images/right.png")
right_button = Button(
    image=right_img, highlightthickness=0, borderwidth=0, command=next_card
)
right_button.grid(column=1, row=1)


window.mainloop()
