from tkinter import *
from tkinter import messagebox
from tkinter import ttk         ##Combobox from the ttk module


def selection():
    messagebox.showinfo("Order", "You ordered " + selected.get())


def clear():
    messagebox.showinfo("Order", "You canceled")
    combobox.current(0)


win = Tk()
win.title("My Combo Box")
win.geometry("300x200")

lbl = Label(win, text="Select Your Choice:")

selected = StringVar()                          ## with readonly state, user can enter random text
combobox = ttk.Combobox(win, width=12, textvariable=selected, state='readonly')
combobox['values'] = ("Cappuccino", "Latte", "Frappuccino", "Smoothie", "Brewed Coffee")
combobox.current(0)

addBtn = Button(win, text="Order", command=selection)
clearBtn = Button(win, text="Clear", command=clear)

lbl.grid(row=0, column=0)
combobox.grid(row=1, column=0)
addBtn.grid(row=2, column=0)
clearBtn.grid(row=2, column=1)

win.mainloop()