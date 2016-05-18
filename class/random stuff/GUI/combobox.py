from tkinter import *
from tkinter import messagebox
from tkinter import ttk



win = Tk()
win.title("My Combo Box")
win.geometry("300x200")


lbl = Label(win, text="Select Your Choice: ")

selected = StringVar()
combobox = ttk.Combobox(win, windth=12, textvariable = selected, state='really')
combobox['values'] = ("Cappuccino", "Latte", "Frappuccino", "Smoothie")
combobox.current(0)


addBtnn = Button(win, text="Order", command=selection)