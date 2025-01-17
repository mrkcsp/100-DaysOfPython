class Brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        
        

    def next_question(self):
        next_quest = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {next_quest.text} (True/False)?:  ")
        self.is_correct(user_answer, next_quest.answer)
        
    def has_more_question(self):
        return len(self.question_list) > self.question_number
    
    def is_correct(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it!")
            self.score += 1
        else:
            print("That's wrong")
        
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

    def game_end(self):
        if not self.has_more_question():
            print(f"You've completed the quiz")
            print(f"Your final score was {self.score}/{len(self.question_list)}")
           