class QuizBrain:

    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.user_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (TRUE or FALSE?): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.user_score += 1
            self.current_score()
            print("You got it right" + ("\n" * 4))
        else:
            self.current_score()
            print("That's wrong" + ("\n" * 4))
        print(f"The correct answer is {correct_answer}")

    def current_score(self):
        print(f"Your current score is {self.user_score} / {self.question_number}")

