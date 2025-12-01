from tkinter import *

def button_click():
    label_text = calculate.get()
    number = float(label_text)
    number *= 1.609344
    kilometer = round(number)
    label_kilometer.config(text=f"{kilometer}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=50)
window.config(padx=25, pady=25)

label = Label()
label.config(text="is equals to")
label.grid(column=0, row=1)

calculate = Entry(justify='center')
calculate.grid(column=2, row=0)

label_kilometer = Label()
label_kilometer.config(text="0")
label_kilometer.grid(column=2, row=1)

button = Button(text="Click Me", command=button_click)
button.grid(column=2, row=2)

label_miles = Label()
label_miles.config(text="Miles")
label_miles.grid(column=3, row=0)

label_km = Label()
label_km.config(text="Kilometers")
label_km.grid(column=3, row=1)

window.mainloop()
