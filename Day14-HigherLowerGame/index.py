import random
import data


def vs_selection(quest):
    if len(quest) > 0:
        selected = random.choice(quest)
        discard = quest.index(selected)
        quest.pop(discard)
        return selected
    else:
        print("No more questions! You win :)")
        return False


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
    
def format_data(account):
    acc_name = account["name"]
    acc_description = account["description"]
    acc_country = account["country"]
    return f"{acc_name}, a {acc_description}, from {acc_country}"
    
print("\n") 
print("Welcome to the Higher - Lower Game!")
print("\n") 
wanna_play = True


while wanna_play == True:
    score = 0
    correct_answer = True
    account_a = vs_selection(data.data)
    while correct_answer == True:
        account_b = vs_selection(data.data)
        if account_b != False:
            print(f"Compare A: {format_data(account_a)}")
            print(f"VS \nAgainst B: {format_data(account_b)}")

            user_choice = input(f"Who has more followers? Type 'A' or 'B':  ")
            correct_answer = comparation(account_a["follower_count"], account_b["follower_count"], user_choice)
            if correct_answer == True:
                if user_choice.lower() == "b":
                    account_a = account_b
                score += 1
                print("\n" * 20)
                print(f"You're Right! Current score: {score}")
            else:
                print("\n" * 2)
                print(f"You lose. You got {score}")


           
    wanna_play = cont_play(input("Wanna play again? 'y' or 'n'"))

