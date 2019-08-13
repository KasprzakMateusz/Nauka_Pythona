from tkinter import *

re_fuel = Tk()
var = IntVar()
var.set(1)

re_fuel.title("Dodaj tankowanie")
re_fuel.geometry("300x170")

def save():
    print("Selection:", var.get())
    re_fuel.destroy()


Radiobutton(re_fuel, text="Diesel", variable=var, value=1).grid(row=6, column=0)
Radiobutton(re_fuel, text="Benzyna", variable=var, value=2).grid(row=6, column=1)
Radiobutton(re_fuel, text="Gaz", variable=var, value=3).grid(row=6, column=2)

Label(re_fuel, text="Litry: ").grid(row=1, column=0, pady=5)
Label(re_fuel, text="Cena: ").grid(row=2, column=0, pady=5)
Label(re_fuel, text="Data: ").grid(row=3, column=0, pady=5)

first = Entry(re_fuel, width=20)
first.grid(row=1, column=1)
second = Entry(re_fuel, width=20)
second.grid(row=2, column=1)
third = Entry(re_fuel, width=20)
third.grid(row=3, column=1)

Button(re_fuel, text="Zapisz", command=save, width=15).grid(row=4, column=1, pady=10)
re_fuel.mainloop()