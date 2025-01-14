import random

cards = {
    "A": 11,
    2 : 2,
    3 : 3,
    4: 4,
    5: 5,
    6: 6, 
    7: 7,
    8: 8,
    9: 9,
    10 : 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


def score_calculator(cards):
    score = 0
    ace = 0
    for card in cards:
        if card[0] == "A":
            ace += 1
        else:
            score += card[1]
    if ace > 0:
        for i in range(ace):
            if score + 11 > 21:
                score += 1
            else:
                score += 11
    return score

def get_random(card):
    return random.choice(list(card.items()))

def game_logic(card):
    user_cards = []
    dealer_cards = []
    for i in range(4):
        if i % 2 == 0:
            user_cards.append(get_random(card))
        else:
            dealer_cards.append(get_random(card))
            
    user_score = score_calculator(user_cards)
    print(f"You have a {user_cards[0][0]} and a {user_cards[1][0]}. You're score is {user_score}")
    print(f"Dealer has {dealer_cards[0][0]} and a covered card")
    
    user_choice = "y"

    while user_choice == "y":
        user_choice = input("'y' if you want another card, 'n' if you want to stop\n")
        if user_choice.lower() == "y":
            another_card = get_random(card)
            user_cards.append(another_card)
            user_score = score_calculator(user_cards)
            print(f"You get a {another_card[0]}")

            if user_score > 21:
                return print(f"Bust! You lose")
            else:
                print(f"You're score is {user_score}")
        else:
            dealer_score = score_calculator(dealer_cards)
            print(f"The Dealer has a {dealer_cards[0][0]} and {dealer_cards[1][0]}. He has {dealer_score}")

            while dealer_score < 17:
                another_card = get_random(card)
                dealer_cards.append(another_card)
                print(f"Gets a card, is a {another_card[0]}")
                dealer_score = score_calculator(dealer_cards)
                
                if dealer_score > 21:
                    return print("Dealer's bust! You Win!")
                else:
                    print(f"The dealer has {dealer_score} points")

    if user_score == dealer_score:
        print("It's a draw!")
    else:             
        print(f"You win with {user_score} points") if user_score > dealer_score else print(f"You lose, the Dealer has {dealer_score}")



game_logic(cards)