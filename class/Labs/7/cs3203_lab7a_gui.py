from tkinter import *
#from tkinter import messagebox

cnt = 1





digit1 = "1"
digit2 = "2"

def changeLabel():
    global cnt
    lbl.configure(text="clicked" + str(cnt) + " times")
    lbl.configure
    return

def clear():
    return





win = Tk()
win.title("Math is fun!")
win.geometry("600x300")



lbl1 = Label(win, text=digit1)
lbl2 = Label(win, text=digit2)
EnterNumbers = Label(win, text="Enter Number")
E1 = Entry(win, bd =5)
mb = Menubutton ( win, text="Operations", relief = RAISED)

#
# addBtn = Button(win, text="Add", command=changeLabel)
# clearBtn = Button(win, text="Clear", command=clear)

lbl1.grid(row=0, column=1)
lbl2.grid(row=0, column=6)
EnterNumbers.grid(row=1,column=0)
E1.grid(row=1, column=1)

mb.grid(row=0, column = 3)
mb.menu = Menu (mb, tearoff = 0)
mb["menu"] = mb.menu

addVar = IntVar()
subVar = IntVar()

mb.menu.add_checkbutton (label = "+", variable= addVar)
mb.menu.add_checkbutton (label = "-", variable= subVar)


# addBtn.grid(row=1, column=0)
# clearBtn.grid(row=1, column=1)

win.mainloop()