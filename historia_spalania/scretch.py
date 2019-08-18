from tkinter import *
from tkinter.ttk import *
from historia_spalania import code

window = Tk()

table = Treeview()
table['columns'] = ('fuel', 'price', 'liter', 'mile_age', 'full' , 'data')
table.heading("#0", text="Nr.")
table.column("#0", width=50, anchor='center')

table.heading("fuel", text="Paliwo")
table.column("fuel", width=100, anchor='center')

table.heading("price", text="Cena")
table.column("price", width=100, anchor='center')

table.heading("liter", text="Litry")
table.column("liter", width=100, anchor='center')

table.heading("mile_age", text="Przebieg")
table.column("mile_age", width=100, anchor='center')

table.heading("full", text="Do pełna")
table.column("full", width=100, anchor='center')

table.heading("data", text="Data")
table.column("data", width=100, anchor='center')

table.grid()
tw = table

for i in range(5):
    tw.insert('','end',text='1', value=(i,'-','-','-','-','-'))

window.mainloop()