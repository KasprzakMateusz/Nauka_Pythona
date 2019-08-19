from tkinter import *
from tkinter import messagebox

from wydatki_procentowe import code

window = Tk()
w_top = Frame(window)
w_top.grid(row=0, column=0, pady=2, padx=2)
w_middle = Frame(window)
w_middle.grid(row=1, column=0, pady=2, padx=2)
w_bottom = Frame(window)
w_bottom.grid(row=2, column=0, pady=2, padx=2)

window.geometry("330x190")
window.title("Kalkulator podziału rat")

Label(w_middle, text="Kwota do podziału ").grid(row=1, column=1, sticky=E)
Label(w_middle, text='Zarobki osoby 1 ').grid(row=2, column=1, sticky=E)
Label(w_middle,text="Zarobki osoby 2 ").grid(row=3, column=1, sticky=E)

e1 = Entry(w_middle, width="20")
e1.grid(row=1, column=2)
e2 = Entry(w_middle, width="20")
e2.insert(END, 2100)
e2.grid(row=2, column=2)
e3 = Entry(w_middle, width="20")
e3.insert(END, 3100)
e3.grid(row=3, column=2)


def send():
    pr = code.Function(float(e2.get()), float(e3.get()), float(e1.get()))

    message_window.delete(0.0, END)
    message_window.insert(END, f'Osoba pierwsza: {round(pr.first_person(),2)} zł\n')
    message_window.insert(END, f'Osoba druga: {round(pr.second_person(),2)} zł')


Button(w_middle, text="Oblicz", width="10", command=send).grid(row=4, column=2, sticky=W)
message_window = Text(w_bottom, width="40", height="5")
message_window.grid(row=5, column=2, sticky=W)



window.mainloop()

