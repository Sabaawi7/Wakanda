from tkinter import *

root = Tk()
Greeting = Label(root, text="Hello User, please press Next and Type in your Name").grid(
    row=0, column=0
)
NameEntry = Entry(root)


def ShowNameInput():
    NameEntry.grid(row=2, column=0)
    FirstSaveClick = Button(root, text="Save", command=SaveUsername).grid(
        row=3, column=0
    )
    ShowListClick = Button(
        root, text="Show List of Usernames", command=printUsernames
    ).grid(row=4, column=0)


FirstNextClick = Button(root, text="Next", command=ShowNameInput).grid(row=1, column=0)

usernames = []


def SaveUsername():
    usernames.append(NameEntry.get())

    def ConfirmAdded():
        printUsername = Label(root, text="added!").grid(row=5, column=0)

    ConfirmAdded()


def printUsernames():
    Users = ""
    for user in usernames:
        Users += user + ", "
    UsernamesLabel = Label(root, text="The Users are %s " % Users).grid(row=6)


root.mainloop()
