from tkinter import *
root = Tk()
v = IntVar()

Radiobutton(root, text="Male", variable=v, value=1).pack()
Radiobutton(root, text="Female", variable=v, value=2).pack()

root.mainloop()
