from tkinter import *
from tkinter import messagebox


def sup():
    print("sup")
    messagebox.showinfo("You clicked sup", "SUP BRO!")
    answer = messagebox.askyesno("Ask Yes No Messagebox", "Do you like stuff?")
    messagebox.askokcancel("OK Cancel", "Delete the item?")
    print(answer)



win = Tk()           # create a root window
win.title("My Button GUI")       #set the title
win.geometry("1024x768")

btn1 = Button(win, text = "Quit", command = win.quit)
btn2 = Button(win, text="sup", command = sup)
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)


win.mainloop()          # start; make it visible