def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")


greet_with_name("Marco")
greet_with_name("Angela")

######################################

def life_in_weeks(age):
    weeks = (90 - age) * 52
    print(f"You have {weeks} weeks left.")
    
life_in_weeks(20)
life_in_weeks(40)
life_in_weeks(70)

######################################

def greet_with(name, location):
    print(f"Hello {name} from {location}")

greet_with("Mia", "Budapest")


def greet_with_fixed(name = "Angela", location = "Rome"):
    print(f"Hello {name} from {location}")

greet_with_fixed()

######################################

def calculate_love_score(name1, name2):
    true_love = (name1 + name2).lower()
    first_digit = 0
    second_digit = 0
    for letter in true_love:
        if letter in "true":
            first_digit += 1
        if letter in "love":
            second_digit += 1
    
    print(f"{first_digit}{second_digit}")

calculate_love_score("George", "Alexandra")