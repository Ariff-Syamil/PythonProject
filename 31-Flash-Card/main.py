from tkinter import *
import pandas, random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
next_text = {}
unknown_text = []
data_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    data_learn = data.to_dict(orient="records")

def change():
    global flip_timer, next_text
    window.after_cancel(flip_timer)
    next_text = random.choice(data_learn)
    canvas.itemconfig(background_image, image=front_card)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(learn_text, text=next_text['French'], fill="black")
    flip_timer = window.after(3000, func=card_late)

def known_card():
    data_learn.remove(next_text)
    unknown_word_df = pd.DataFrame(data_learn)
    unknown_word_df.to_csv("./data/words_to_learn.csv", index=False)
    change()

def card_late():
    canvas.itemconfig(background_image, image=back_card)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(learn_text, text=next_text['English'], fill="white")

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=card_late)

canvas = Canvas(width= 800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
background_image = canvas.create_image(400, 265, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)

language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
learn_text = canvas.create_text(400, 263, text="", font=("Ariel",60,"bold"))

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image,bg=BACKGROUND_COLOR, highlightthickness=0, command=known_card)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0,command=change)
wrong_button.grid(column=0, row=1)

change()

window.mainloop()