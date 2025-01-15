import random
import data


def vs_selection(quest):
    try:
        selected = random.choice(quest)
        discard = quest.index(selected)
        quest.pop(discard)
        return selected
    except IndexError:
        print("No more questions! You win :)")


def comparation(a, b , choice):
    if choice.lower() == "a":
       return True if a > b else False 
    else:
        return True if a < b else False        
    

def cont_play(play):
    if play == "y":
        print("Let's play again... Here we go!")
        return True
    else:
        print("See you soon!")
        return False
    
print("\n") 
print("Welcome to the Higher - Lower Game!")
print("\n") 
wanna_play = True


while wanna_play == True:
    score = 0
    correct_answer = True
    a = vs_selection(data.data)
    while correct_answer == True:
        print(f"Compare A: {a["name"]}, {a["description"]}, from {a["country"]}")
        b = vs_selection(data.data)
        print(f"VS \nAgainst B: {b["name"]}, {b["description"]}, from {b["country"]}")

        user_choice = input(f"Who has more followers? Type 'A' or 'B':  ")
        correct_answer = comparation(a["follower_count"], b["follower_count"], user_choice)
        if correct_answer == True:
            if user_choice.lower() == "b":
                a = b
            score += 1
            print("\n" * 20)
            print(f"You're Right! Current score: {score}")
        else:
            print("\n" * 2)
            print(f"You lose. You got {score}")

           
    wanna_play = cont_play(input("Wanna play again? 'y' or 'n'"))

