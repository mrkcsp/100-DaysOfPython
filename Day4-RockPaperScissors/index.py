import random

possible_choices = ["rock", "paper", "scissors"]
user_choice = int(input("Type 0 for rock, 1 for paper or 2 for scissors:\n"))
ai_choice = random.randint(0, 2)

print(f"Computer chose -> {possible_choices[ai_choice]}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and ai_choice == 2:
    print("You Win!")
elif ai_choice == 0 and user_choice == 2:
    print("You Lose!")
elif ai_choice > user_choice:
    print("You Lose!")
elif ai_choice < user_choice:
    print("You Win!")
elif ai_choice == user_choice:
    print("It's a Draw!")




