from tkinter import *

root =Tk()

mb = Menubutton(root, text="Click Here")
mb.pack()

menu = Menu(mb, tearoff =0)
mb.config(menu=menu)
menu.add_command(label="About")
menu.add_command(label="Help")

root.mainloop()