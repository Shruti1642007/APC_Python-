from tkinter import *
root = Tk()
root.title("Entry Widget")
root.geometry("300x200")

entry = Entry(root)
entry.pack()

def show():
    Label(root, text="Hello " + entry.get()).pack()

Button(root, text="Submit", command=show).pack()    

root.mainloop()
