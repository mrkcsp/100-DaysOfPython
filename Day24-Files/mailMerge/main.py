#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter_template = "./Input/Letters/starting_letter.txt"
names_list = "./Input/Names/invited_names.txt"


def read(filename):
    with open(filename, "r") as file:
        content = file.read()
    return content

def read_lines(filename):
    stripped_names = []
    with open(filename, "r") as file:
        all_names = file.readlines()
        for name in all_names:
            stripped_names.append(name.strip())
    return stripped_names
    
def write(content, name):
    with open(f"./Output/ReadyToSend/letter_for_{name}", "w") as file:
        updated_file = content.replace("[name]", name)
        file.write(updated_file)


template = read(letter_template)
names = read_lines(names_list)
for name in names:
    write(template, name)
 
