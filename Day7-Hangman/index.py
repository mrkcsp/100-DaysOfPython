import random

word_list = [
    'emerald', 'nostalgia', 'optimism', 'xenon', 'umbrella', 'violet', 'piano', 'passion',
    'lemon', 'quest', 'serenity', 'lighthouse', 'ocean', 'bridge', 'resilience', 'harmony',
    'knowledge', 'jungle', 'banana', 'kite', 'night', 'zebra', 'mountain', 'horizon',
    'cherry', 'elephant', 'wanderlust', 'zeal', 'giraffe', 'castle', 'river', 'tiger',
    'journey', 'imagine', 'glacier', 'unity', 'xylophone', 'adventure', 'yearning', 'diamond',
    'apple', 'whisper', 'falcon', 'queen', 'sunshine', 'victory', 'tranquility', 'island',
    'date', 'forest'
]

def hangaman(words):
    lifes = 6
    word_to_find = random.choice(words)
    print(word_to_find)
    guessed_word = ["_"] * len(word_to_find)
    guessed_letters = []
    print("The game is ready. Good Luck!")

    while lifes > 0 and "_" in guessed_word:
        print(f"The word to guess is {guessed_word}")
        user_char_input = input("Insert a char to check:\n")
        if len(user_char_input) > 1 and user_char_input.isalpha():
            print("Insert a unique valid char please")
        
        if user_char_input in guessed_letters:
            print(f"You already tried '{user_char_input}' char")

        if user_char_input in word_to_find:
            print(f"Yes! The '{user_char_input}' is in the word!")
            for i, char in enumerate(word_to_find):
                if char == user_char_input:
                    guessed_word[i] = user_char_input
        else:
            lifes -= 1
            print(f"Oh no! The '{user_char_input}' is not in the word :(")
            print(f"######## lifes {lifes}/6 ########")

    if "_" in guessed_word:
        print(f"\n Sorry, You lose... The word was '{word_to_find}'")
    else:
        print(f"\n Wow! You win! The word was '{word_to_find}'")



hangaman(word_list)