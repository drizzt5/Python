from tkinter import *
from tkinter import messagebox

def hello():
    print("Hello")
    messagebox.showinfo("Show Info Messagebox", "You clicked the Hello button")
    answer = messagebox.askyesno("Ask Yes No Messagebox", "Do you like coffee?")
    print(answer)

win = Tk()
win.title("My Button GUI")
win.geometry("400x300")      ##this is how you size the window

btn1 = Button(win, text="Hello", command=hello)
btn2 = Button(win, text="Quit", command=win.quit)
btn1.pack()
btn2.pack()

win.mainloop()