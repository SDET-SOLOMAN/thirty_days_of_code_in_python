from behind_the_game import Question
from data import question_data
from quizBrain import QuizBrain

question_bank = []

for num in question_data:
    my_retrive = Question(num["question"], num["correct_answer"])
    question_bank.append(my_retrive)

quiz = QuizBrain(question_bank)
quiz.next_question()