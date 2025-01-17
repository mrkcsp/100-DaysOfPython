from question_model import Question
from data import question_data
from quiz_brain import Brain

question_bank = []
for question in question_data:
    quest_text = question["text"]
    quest_answer = question["answer"]
    new_question = Question(quest_text, quest_answer)
    question_bank.append(new_question)


# print(question_bank)
# print(question_bank[0].answer)


quiz = Brain(question_bank)

while quiz.has_more_question():
    quiz.next_question()
    quiz.game_end()
