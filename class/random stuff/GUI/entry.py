from tkinter import *
from tkinter import messagebox

def greeting():
    messagebox.showinfo("Greeting", "Nice to meet you " + namevar.get())
    clear()

def clear():
    entry.delete(0, END)

win = Tk()
win.title("My Entry Box")
win.geometry("300x200")

lbl = Label(win, text="Enter your name: ")

namevar = StringVar()
entry = Entry(win, width=12, textvariable=namevar)

addBtn = Button(win, text="Submit", command=greeting)
clearBtn = Button(win, text="Clear", command=clear)

lbl.grid(row=0, column=0)
entry.grid(row=1, column=0)
addBtn.grid(row=2, column=0)
clearBtn.grid(row=2, column=1)

win.mainloop()