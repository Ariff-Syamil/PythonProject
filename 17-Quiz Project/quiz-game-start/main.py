from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question = Question(data["question"], data["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_have_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")