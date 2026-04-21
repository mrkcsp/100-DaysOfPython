# ---------------------------- PASSWORD GENERATOR ------------------------------- #


from random import choice, randint, shuffle
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

FILE_NAME = "data.json"

def random_pass_gen():
    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    nr_symbols = randint(2,4)
    nr_numbers = randint(2,4)

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    pass_list = password_letters + password_symbols + password_numbers

    shuffle(pass_list)

    pass_mixed = "".join(pass_list)
    
    input_password.delete(0, END)
    input_password.insert(0, pass_mixed)

    pyperclip.copy(pass_mixed)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search():
    website = input_website.get()
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            #print(data)
    except FileNotFoundError:
        messagebox.showerror(title="Not found!", message="The file or the data was not found")
    else: 
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}" )
        else:
            messagebox.showinfo(title=website, message=f"No data found for this website" )


    

# ---------------------------- SAVE PASSWORD ------------------------------- #

from tkinter import messagebox
import json

def save_pass():
    
    website_data = input_website.get()
    email_username_data = input_email_username.get()
    password_data = input_password.get()

    new_data = {website_data: {
         "email": email_username_data,
         "password": password_data
        }
    }

    if len(website_data) < 4 or len(email_username_data) < 2 or len(password_data) < 4:
            messagebox.showwarning(title="Oooops!", message=f"The fields cannot be empty or too short, check if: " 
                               f"\n-Website is minimum 5 characters \n-email/username is minimum 3 characters \n-password is minimum 5 characters\n")    
            
    else:
        try:
            with open(FILE_NAME, "r") as file:
                #json.dump(new_data, file, indent=4) # "w" mode

                data = json.load(file) # "r" mode
                #print(data)
                data.update(new_data)
        except FileNotFoundError:
             print("il file non esiste")
             with open(FILE_NAME, "w") as file:    
                json.dump(new_data, file, indent=4)
        else:
            with open(FILE_NAME, "w") as file:    
                json.dump(data, file, indent=4)

                input_website.delete(0, END)
                input_website.delete(0, END)

        messagebox.showinfo(title="Data saved", message=f"Your data was saved on the file: {FILE_NAME}" )




# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Password Manager")
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img) #x and y position for center is the half of all
canvas.grid(row=0, column=1) 
window.config(padx=50, pady=50)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)


input_website = Entry(width=21)
input_website.grid(row=1, column=1, columnspan=1)
input_website.focus()
search_button =  Button(text="Search", width=13, command=search)
search_button.grid(row=1, column=2)
input_email_username = Entry(width=35)
input_email_username.grid(row=2, column=1, columnspan=2)
input_email_username.insert(0, "mrk@iclud.ct")
input_password = Entry(width=21)
input_password.grid(row=3, column=1)
gen_password = Button(text="Generate Password", command=random_pass_gen)
gen_password.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()