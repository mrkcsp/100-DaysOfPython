#list
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def unified_encrypt_decrypt(word, shift, encode_or_decode):
    message = ""
    for char in word:
        if char not in chars:
            message += char
        else:
            if encode_or_decode.lower() == "encrypt":
                position = chars.index(char) + shift
            else:
                position = chars.index(char) - shift
            position %= len(chars)
            message += chars[position]
    return print(f"Crypted message is: {message}")

user_want_continue = "yes"

while user_want_continue.lower() == "yes":
    user_choice = input("Do you want 'encrypt' or 'decrypt'?\n")
    if user_choice.lower() == "encrypt":
        user = input("Insert a message to encrypt:\n")
        shift_amount = int(input("select the shift:\n"))
        unified_encrypt_decrypt(user, shift_amount, "encrypt")

    elif user_choice.lower() == "decrypt":
        user = input("Insert a message to decrypt:\n")
        shift_amount = int(input("select the shift:\n"))
        unified_encrypt_decrypt(user, shift_amount, "")

    else:
        print("Something went wrong! Retry")

    user = ""
    user_want_continue = input("You want to continue? Please provide a 'yes' or 'no'\n")

print("Good bye!")