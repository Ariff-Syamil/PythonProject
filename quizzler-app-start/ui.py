from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ["Arial",20,"Italic"]
class QuizInterface:

    def __init__(self, quiz_bank: QuizBrain):
        self.quiz = quiz_bank

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")

        self.question_text = self.canvas.create_text(150,125,width=280,text="Questions", fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=15)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, fg=THEME_COLOR, command=self.true_answer)
        self.true_button.grid(row=2, column=0, pady=15)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, fg=THEME_COLOR, command=self.false_answer)
        self.false_button.grid(row=2, column=1, pady=15)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.label.configure(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.configure(state="disabled")
            self.false_button.configure(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.update_score(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.update_score(is_right)

    def update_score(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
            # score += 1
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
        # self.label.configure(text=f"Score: {score}")


