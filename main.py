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
quiz.next_question()

