from tkinter import *

root = Tk()
root.minsize(width=350,height=200)
root.title("Miles to Kilometers")
root.config(padx=40, pady=40)

def calculate():
    miles = float(entry.get())
    kilometers = miles * 1.689, 2
    km_result.config(text=kilometers)

default = 0

entry = Entry(width=15)
entry.grid(column=1, row=0)

miles = Label(text="Miles", font=("arial", 16))
miles.grid(column=3, row=0)

is_equal = Label(text="is equal to", font=("arial", 16))
is_equal.grid(column=0, row=2)

km_result = Label(text=default, font=("arial", 16))
km_result.grid(column=1, row=2)

km = Label(text="Km", font=("arial", 16))
km.grid(column=3, row=2)

btn = Button(text="Calculate", command=calculate)
btn.grid(column=1, row=4)
root.mainloop()
