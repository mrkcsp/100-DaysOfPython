import random

secret = random.randint(1, 100)

def check_num(attempt, num):
    if num == attempt:
        print(f"Oh yes, it's {num}. You win!")
        return True
    elif num > attempt:
        print("Too low.")
        return False
    elif num < attempt:
        print("Too high.")
        return False
    
def difficulty_selection(diff):
    if diff.lower() == "easy":
        return  10
    elif diff.lower() == "hard":
        return 5

print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':   ")
attempts = difficulty_selection(difficulty)


win = False
while attempts > 0 and win != True:
    print(f"You have {attempts} attempts to guess the number.")
    user_number = int(input(f"Try a number:\n"))
    win = check_num(user_number, secret)
    if win == False:
        attempts -= 1
    if attempts == 0:
        print(f"You lose. The number was {secret}.")
