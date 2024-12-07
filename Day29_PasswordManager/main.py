from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = website_entry.get()
    website_entry.delete(0, END)
    username = username_entry.get()
    username_entry.delete(0, END)
    password = password_entry.get()
    password_entry.delete(0, END)
    with open("./Day29_PasswordManager/data.txt", "a") as f:
        f.write(f"{website} | {username} | {password}\n")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="./Day29_PasswordManager/logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text=r"Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=40)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
