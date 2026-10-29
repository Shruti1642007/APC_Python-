from tkinter import *

root =Tk()

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

lb = Listbox(root, yscrollcommand=scroll.set)

for i in range(20):
    lb.insert(END, "python" + str(i))

lb.pack()
scroll.config(command=lb.yview)
root.mainloop()
