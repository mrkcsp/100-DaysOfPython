import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = tkinter.Label(text="I'm a Label", font=("Arial", 24, "bold"))
# label.pack(side="left")
label.grid(column=0, row=0)

#button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    label["text"] = new_text
    
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=0)

#entry

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()

