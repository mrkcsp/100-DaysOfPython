from tkinter import *
import pandas
import random
import time

current_card = {}
to_learn = {}

try: 
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


#print(to_learn)

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_language, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")  
    canvas.itemconfig(card_background, image=card_front)
    window.after(3000, func=flip_card)
    

def flip_card():
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")  
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME= "Ariel"

window = Tk()
window.title("Flash Cards")

flip_timer = window.after(3000, func=flip_card)

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back= PhotoImage(file="images/card_back.png")
check_image = PhotoImage(file="images/right.png")
cross_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front) #x and y position for center is the half of all
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0) # box around the canvas (highlightthickness)

card_language = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=(FONT_NAME, 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

know_button = Button(image=check_image, highlightthickness=0, command=is_known)
know_button.grid(row=1, column=1)


    

next_card()


window.mainloop()
