from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    question_bank.append(Question(text, answer))


print(question_bank[3].text)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You Completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")

