from tkinter import *

root = Tk()
root.title("Students book")
Students = []
# Labels
StudentName = Label(root, text="Student's Name:")
Homework = Label(root, text="Homework's grades seperated by a comma:")
Quizzes = Label(root, text="Quizzes' grades sepertated by a comma:")
Tests = Label(root, text="Tests' grades seperated by a comma:")

StudentName.grid(row=0, column=0)
Homework.grid(row=1, column=0)
Quizzes.grid(row=2, column=0)
Tests.grid(row=3, column=0)

# Input Fields
NameEntry = Entry(root).grid(row=0, column=1)
HomeworkEntry = Entry(root).grid(row=1, column=1)
QuizzesEntry = Entry(root).grid(row=2, column=1)
TestsEntry = Entry(root).grid(row=3, column=1)

# Functions
def SaveData(name, HW, Q, T):
    name: {"Name": name, "Homework": [HW], "Quizzes": [Q], "Tests": [T]}
    Students.append(name)
    if Students[0] is not None:
        ConfirmSave()


def ConfirmSave():
    Confirmation = Label(root, text="Student added!").grid(columnspan=2)


# Buttons

Save = Button(
    root,
    text="Save",
    padx=168,
    pady=10,
    command=lambda: SaveData(
        NameEntry.get(), HomeworkEntry.get(), QuizzesEntry.get(), TestsEntry.get()
    ),
).grid(columnspan=2)
root.mainloop()
