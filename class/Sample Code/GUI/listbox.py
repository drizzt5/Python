from tkinter import *
from tkinter.messagebox import *

def selection(event):
    print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))
    index = listbox.curselection() ##return multiple indexes if multiple selection is allowed
    print(index[0])

    if index != ():
        value = listbox.get(index)
        showinfo("Selection", value + " is selected")


win = Tk()
win.title("My List Box")
win.geometry("300x300")

scrollbar = Scrollbar(win, orient=VERTICAL)
lbl = Label(win, text="Prog Lang")
listbox = Listbox(win, selectmode=SINGLE, yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

languages = "Java PHP Javascript PL/I Python Scala Lisp Pascal Algol Fortran Cobol C C++".split( )
for lang in languages:
    listbox.insert(END, lang)  ## insert next item at the end of list


listbox.bind("<<ListboxSelect>>", selection)


lbl.grid(row=0, column=0)
listbox.grid(row=1, column=1)
scrollbar.grid(row=1, column=2, sticky=N+S) ##sticky property is critical


win.mainloop()