from tkinter import *
from tkinter import messagebox
from historia_spalania import code


def create_database():
    q = code.Queries()
    q.create_table()
    q.sql_query(q.connection, q.create_table_fuel_usage)


create_database()
window = Tk()
window.title("Kalkulator spalania")
window.geometry("520x400")
window.resizable("false", "false")


# New Window
def refuel():
    re_fuel = Toplevel(window)
    message_box.delete(first=0, last=100)
    message_box.insert(END, "Dodawanie tankowania...")
    message_boxes.delete(0.0, END)


    var = IntVar()
    var.set(1)
    var1 = IntVar()
    var.set(0)

    re_fuel.title("Dodaj tankowanie")
    re_fuel.geometry("300x250")

    def save():

        if var1.get() == 1:
            full = 'Tak'
        else:
            full = "Nie"

        if var.get() == 1:
            fuel = "Diesel"
        elif var.get() == 2:
            fuel = "Benzyna"
        elif var.get() == 3:
            fuel = "Gaz"
        else:
            fuel = None

        if fuel:
            test = f'Rodzaj paliwa: {fuel} \nPrzebieg: {mile_age.get()} \nLitry: {liter.get()} ' \
                   f'\nCena: {price.get()} \nData: {date.get()} \nDo pełna?: {full}'

            fills = (fuel, str(liter.get()).replace(',', '.'), str(price.get()).replace(',', '.'),
                     date.get(), mile_age.get(), full)
            q = code.Queries()
            q.add_refueling(q.connection, fills)

            message_boxes.delete(0.0, END)
            message_boxes.insert(END, test)
            re_fuel.destroy()
        else:
            messagebox.showinfo("Error", "Nie podałeś rodzaju paliwa!")

    Checkbutton(re_fuel, text="Do pełna?", variable=var1).grid(row=7, column=0)

    Radiobutton(re_fuel, text="Diesel", variable=var, value=1).grid(row=0, column=0)
    Radiobutton(re_fuel, text="Benzyna", variable=var, value=2).grid(row=0, column=1)
    Radiobutton(re_fuel, text="Gaz", variable=var, value=3).grid(row=0, column=2, pady=15)

    Label(re_fuel, text="Przebieg: ").grid(row=1, column=0, pady=5)
    Label(re_fuel, text="Litry: ").grid(row=2, column=0, pady=5)
    Label(re_fuel, text="Cena: ").grid(row=3, column=0, pady=5)
    Label(re_fuel, text="Data: ").grid(row=4, column=0, pady=5)

    mile_age = Entry(re_fuel, width=20)
    mile_age.grid(row=1, column=1)
    liter = Entry(re_fuel, width=20)
    liter.grid(row=2, column=1)
    price = Entry(re_fuel, width=20)
    price.grid(row=3, column=1)
    date = Entry(re_fuel, width=20)
    date.grid(row=4, column=1)

    Button(re_fuel, text="Zapisz", command=save, width=15).grid(row=5, column=1, pady=10)
    re_fuel.mainloop()


def stats():
    message_box.delete(first=0, last=100)
    message_box.insert(END, "Statystyki tankowania")
    message_boxes.delete(0.0, END)
    q = code.Queries()
    message_boxes.insert(END, q.sum_of_refuel(q.connection))


def history():
    message_box.delete(first=0, last=100)
    message_box.insert(END, "Historia tankowania")
    message_boxes.delete(0.0, END)
    q = code.Queries()
    for i in q.show_db(q.connection):
        message_boxes.insert(END, i)


def close():
    window.destroy()
    exit()


# Frames
top_frame = Frame(window, borderwidth=2, pady=5)
mid_frame = Frame(window, borderwidth=2, pady=5)
bottom_frame = Frame(window, borderwidth=2, pady=5)

top_frame.grid(row=0, column=0)
mid_frame.grid(row=1, column=0)
bottom_frame.grid(row=2, column=0)

# Labels
message = Label(top_frame, text="Witaj w kalkulatorze spalania", font="None 12 bold")
message.grid()

# Buttons
refuel = Button(mid_frame,text="Dodaj Tankowanie", command=refuel, width=20)
stats = Button(mid_frame, text="Statystyki", command=stats, width=20)
history = Button(mid_frame, text="History", command=history, width=20)
close = Button(bottom_frame, text="Exit", command=close, width=30)

refuel.grid(row=1, column=0, padx=10)
stats.grid(row=1,column=1, padx=10)
history.grid(row=1,column=2, padx=10)
close.grid(row=4,column=1, padx=10)

# Text Entry (1 line text slot)
message_box = Entry(bottom_frame, width=80)
message_box.grid(row=1, column=1, pady=10)

# Text (more than 1 text slot)
message_boxes = Text(bottom_frame, height=13,width=60)
message_boxes.grid(row=2, column=1, pady=10)

if __name__ == "__main__":
    window.mainloop()


