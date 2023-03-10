class QuizBrain:

    def __init__(self, q_l):
        self.question_number = 0
        self.question_list = q_l

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (TRUE or FALSE?): ")
        # self.check_answer(user_answer, current_question.answer)