class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.current_score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return True if (self.question_number != len(self.question_list)) else False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False) ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.current_score += 1
        else:
            print(f"You got it wrong, the correct answer is: {correct_answer}")
        print(f"Your current score is:{self.current_score}/{self.question_number}\n")

