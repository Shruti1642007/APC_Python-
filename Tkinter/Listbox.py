from tkinter import *

root = Tk()
lb = Listbox(root)

lb.insert(1, "python")
lb.insert(2, "java")
lb.insert(3, "c++")
lb.pack()
root.mainloop()
