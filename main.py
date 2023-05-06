from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# making list of Question objects that store text and answers form questions in question_data
question_bank = []

for question in question_data:
    q = Question(question["text"], question["answer"])
    question_bank.append(q)

# creating QuizBrain object and using its methods to let user play Quiz Game
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

quiz_brain.game_ended()