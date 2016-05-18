from tkinter import *
from tkinter import messagebox

cnt = 1
originalTxt = "Text Message Here"

def changeLabel():
    global cnt
    # messagebox.showinfo("Show Info Messagebox", "You clicked the button")
    lbl.configure(text="Clicked " + str(cnt) + "times")
    lbl.configure(foreground='red')
    cnt += 1

def clear():
    global cnt
    cnt = 0
    lbl.configure(text=originalTxt)
    lbl.configure(foreground='black')

win = Tk()
win.title("My Grid Layout")
win.geometry("300x200")

lbl = Label(win, text=originalTxt)
addBtn = Button(win, text="Add", command=changeLabel)
clearBtn = Button(win, text="Clear", command=clear)

lbl.grid(row=0, column=0)
addBtn.grid(row=0, column=1)
clearBtn.grid(row=0, column=2)

win.mainloop()