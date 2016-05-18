from tkinter import *
from tkinter import messagebox


def sup():
    print("sup")
    messagebox.showinfo("You clicked sup", "OK")



win = Tk()           # create a root window
win.title("My Button GUI")       #set the title

label = Label(win)
label.config(text="\n Sup, this is my first GUI. So far this is all I know.\n")

## Without packing a label won't appear
label.pack(side=BOTTOM, expand=NO)   #options aren't necessary, but I wanted to try them


win.mainloop()          # start; make it visible