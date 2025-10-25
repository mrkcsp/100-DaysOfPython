import tkinter

window = tkinter.Tk()

window.title("Mile to Kilometer Converter")
window.minsize(width=100, height=100)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = tkinter.Label(text="0")
result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

def calculate():
    km = input.get()
    km = float(km) * 1.60934
    km = round(km, 2)
    result_label["text"] = km


calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()