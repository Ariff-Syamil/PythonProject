from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None
mark = ""

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    global reps, mark
    window.after_cancel(timer)
    reps = 0
    mark = ""
    canvas.itemconfig(timer_display, text="00:00")
    label_timer.config(text="TIMER", fg=GREEN)
    right_timer.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer_start():
    global reps
    reps += 1
    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        label_timer.config(text="L_BREAK", fg=RED)
    elif reps % 2 == 0:
        label_timer.config(text="S_BREAK", fg=PINK)
        count_down(short_break)
    else:
        label_timer.config(text="WORK", fg=GREEN)
        count_down(work_min)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global mark
    count_hours = math.floor(count / 60)
    count_minutes = round(count % 60, 2)
    if count_hours < 10:
        count_hours = f"0{count_hours}"
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"

    canvas.itemconfig(timer_display, text=f"{count_hours}:{count_minutes}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 100)
    elif count == 0:
        timer_start()
        if reps % 2 == 0:
            mark += "✓"
            right_timer.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=25, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato)
timer_display = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

label_timer = Label(text="TIMER", bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 30, 'bold'))
label_timer.config(fg=GREEN)
label_timer.grid(column=1, row=0)

right_timer = Label(bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 10, 'bold'))
right_timer.config(fg=GREEN)
right_timer.grid(column=1, row=2)

start = Button(text="Start", highlightthickness=0 ,command=timer_start)
start.config(font=(FONT_NAME,9))
start.grid(column=0, row=2)

start = Button(text="Reset", highlightthickness=0, command=timer_reset)
start.config(font=(FONT_NAME,9))
start.grid(column=2, row=2)

window.mainloop()