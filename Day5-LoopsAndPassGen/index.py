#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password_easy = ""

for char in range(0, nr_letters):
    password_easy += random.choice(letters)

for char in range(0, nr_symbols):
        password_easy += random.choice(symbols)


for char in range(0, nr_numbers):
        password_easy += random.choice(numbers)


print(f"An easy password : {password_easy}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_hard = ""

grouped = [letters, symbols, numbers]

how_many_times = nr_letters + nr_symbols + nr_numbers
for round in range(0, how_many_times):
    type_of_char = random.choice(grouped)
    password_hard += random.choice(type_of_char)

print(f"A hard password : {password_hard}")


#OR
pass_list = []

for char in password_easy:
    pass_list.append(char)

random.shuffle(pass_list)

pass_mixed = ""
for char in pass_list:
      pass_mixed += char

print(f"Mixed easy to get harder password : {pass_mixed}")