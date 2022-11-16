import tkinter
from tkinter import *
root = tkinter.Tk()
def myClick():
    printmsg = Label(root, text ="Du Hurensohn!").grid(column=1)
myName = Label(root, text="Hello World").grid(row=0, column=0)
myButton = Button(root, text="click me to get Insulted!", command=myClick).grid(row=1,column=1)
root.mainloop()