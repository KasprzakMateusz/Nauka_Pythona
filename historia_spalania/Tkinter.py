from tkinter import *
from historia_spalania import code

window = Tk()
window.title("Kalkulator spalania")
window.geometry("520x300")
window.resizable("false", "false")


def refuel():
    message_box.delete(first=0, last=100)
    message_box.insert(END, "Dodawanie tankowania...")
    message_boxes.delete(0.0, END)
    refuel = Tk()
    refuel.title("Dodaj tankowanie")
    refuel.geometry("300x150")

    Label(refuel, text="Litry: ").grid(row=1,column=0,pady=5)
    Label(refuel, text="Cena: ").grid(row=2,column=0)

    Entry(refuel, width=20).grid(row=1, column=1)
    Entry(refuel, width=20).grid(row=2, column=1)

    Radiobutton(refuel, text="Diesel", value=1).grid(row=0, column=0)
    Radiobutton(refuel, text="Benzyna", value=2).grid(row=0, column=1)
    Radiobutton(refuel, text="Gaz", value=3).grid(row=0, column=2)
    def save():
        refuel.destroy()

    Button(refuel, text="Zapisz", command=save, width=15).grid(row=3, column=1, pady=10)
    refuel.mainloop()

def stats():
    message_box.delete(first=0, last=100)
    message_box.insert(END, "Statystyki tankowania")
    message_boxes.delete(0.0, END)
    q = code.Queries()
    message_boxes.insert(END, q.show_db(q.connection))
def history():
    message_box.delete(first=0, last=100)
    message_box.insert(END, "Historia tankowania")
    message_boxes.delete(0.0, END)
    message_boxes.insert(END, "History")
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
message_boxes = Text(bottom_frame, height=5,width=60)
message_boxes.grid(row=2, column=1, pady=10)

window.mainloop()