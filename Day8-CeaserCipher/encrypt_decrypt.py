chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(word, shift):
    encrypted = ""
    for char in word:
        position = chars.index(char)
        position %=  len(chars)
        encrypted += chars[position + shift]
    return print(f"Crypted message is: {encrypted}")

def decrypt(word, shift):
    decrypted = ""
    for char in word:
        position = chars.index(char) - shift
        position %= len(chars)
        decrypted += chars[position - shift]
    return print(f"Decrypted message is: {decrypted}")


user_want_continue = "yes"

while user_want_continue.lower() == "yes":
    user_choice = input("You want 'encrypt' or 'decrypt'?\n")
    if user_choice.lower() == "encrypt":
        user = input("Insert a message to encrypt:\n")
        shift_amount = int(input("select the shift:\n"))
        encrypt(user, shift_amount)

    elif user_choice.lower() == "decrypt":
        user = input("Insert a message to decrypt:\n")
        shift_amount = int(input("select the shift:\n"))
        decrypt(user, shift_amount)

    else:
        print("Something went wrong! Retry")

    user_want_continue = input("You want to continue? Please provide a 'yes' or 'no'\n")

print("Good bye!")