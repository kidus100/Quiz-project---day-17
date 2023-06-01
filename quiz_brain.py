class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.quiz_score = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list)-1:
            return True
        else:
            return False


    def next_question(self):
        self.question_number += 1
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.quiz_score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}")
        print(f"your current score is: {self.quiz_score}/{self.question_number}")
        print("\n")



