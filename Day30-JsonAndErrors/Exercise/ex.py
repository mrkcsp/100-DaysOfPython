# with open("a_file.txt") as f:
#     content = f.read()

# #KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# #IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# #TypeError
# text = "abc"
# print(text + 5)



# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["non_existent_key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key '{error_message}' does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print(f"File was closed.")
#     raise KeyError("Thi is an error that I made up")



heigth = float(input("Heigth: "))
weigth = int(input("Weigth: "))

if heigth > 3:
    raise ValueError("Human heigth should not be over 3 meters")

bmi = weigth / heigth ** 2

print(bmi)
