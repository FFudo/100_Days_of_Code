import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH DATA ------------------------------- #
def search_data():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Ooops", message="Please enter a website.")
    else:
        try:
            with open("./Day29and30_PasswordManager/data.json", "r") as f:
                data = json.load(f)
        except:
            messagebox.showinfo(title="Ooops", message="No data file found.")
        else:
            try:
                username = data[website]["username"]
                password = data[website]["password"]
            except KeyError:
                messagebox.showinfo(
                    title="Ooops", message="There is no entry for this website."
                )
            else:
                messagebox.showinfo(
                    title="Website Entry",
                    message=f"Username: {username}\n Password: {password}",
                )


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {"username": username, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Ooops", message="Please enter a website and password."
        )
    else:
        website_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        try:
            with open("./Day29and30_PasswordManager/data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("./Day29and30_PasswordManager/data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("./Day29and30_PasswordManager/data.json", "w") as f:
                json.dump(data, f, indent=4)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="./Day29and30_PasswordManager/logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text=r"Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=40)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

search_button = Button(text="Search", command=search_data)
search_button.grid(column=2, row=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
