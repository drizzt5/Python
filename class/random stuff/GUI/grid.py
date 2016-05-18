from tkinter import *
from tkinter import messagebox

cnt = 1
originalTxt = "hi"


def changeLabel():
    global cnt
    lbl.configure(text="clicked" + str(cnt) + " times")
    lbl.configure
    return

def clear():
    return





win = Tk()
win.title("My Grid Layout")
win.geometry("300x200")


lbl = Label(win, text=originalTxt)
addBtn = Button(win, text="Add", command=changeLabel)
clearBtn = Button(win, text="Clear", command=clear)

lbl.grid(row=0, column=0)
addBtn.grid(row=1, column=0)
clearBtn.grid(row=1, column=1)

win.mainloop()