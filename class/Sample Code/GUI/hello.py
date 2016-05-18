from tkinter import *

win = Tk()
win.title("My Second GUI")

label = Label(win)
label.config(text='Hello world!')


## Without packing, a label won't appear ##
## try different packing options ##
label.pack()

# label.pack(side=TOP, expand=YES)     ## YES, BOTTOM, TOP, etc are constants defined in tkinter
# label.pack(side=TOP, expand=NO)
# label.pack(side=BOTTOM, expand=YES)
# label.pack(side=BOTTOM, expand=NO)
# label.pack(side=LEFT, expand=YES)
# label.pack(side=LEFT, expand=NO)
# label.pack(side=RIGHT, expand=YES)
# label.pack(side=RIGHT, expand=NO)


win.mainloop()