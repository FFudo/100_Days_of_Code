from tkinter import *


def button_callback():
    new_output = round(int(input.get()) * 1.609, 2)
    output_label.config(text=new_output)


window = Tk()
window.title("Miles to Km Converter")


input = Entry()
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

output_label = Label()
output_label.grid(column=1, row=1)

equal_label = Label(text="is euqal to")
equal_label.grid(column=0, row=1)

button = Button(text="Calculate", command=button_callback)
button.grid(column=1, row=2)

window.mainloop()
