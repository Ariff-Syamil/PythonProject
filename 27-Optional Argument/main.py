from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=600, height=300)

def button_click():
    label_text = input.get()
    my_label.config(text=label_text)

my_label = Label(text="This is a label", font=("Arial",24))
my_label.pack()

button = Button(text="Click Me", command=button_click)
button.pack()

input = Entry()
input.pack()

window.mainloop()