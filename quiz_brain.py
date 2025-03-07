class QuizBrain:
    
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
    
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number + 1}: {question.text}. (True/False)?: ")