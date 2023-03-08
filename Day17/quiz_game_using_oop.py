from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for char in question_data:
    question_text = char['question']
    question_answer = char['correct_answer']
    new_questions = Question(question_text, question_answer)
    question_bank.append(new_questions)

quiz = QuizBrain(question_bank)

quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the game")
print(f"The final score is {quiz.user_score} out of {quiz.question_number}")