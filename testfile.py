Students = []


def AddStudent():
    print("Please type in student name")
    name = input()
    Students.append(name)
    print("Thanks, do you want to make a dictionary for yourself?")
    a = input()
    if a == "yes":
        print("please type your age")
        age = input()
        print("what city do you live in?")
        city = input()
        name = {"Name": name, "Age": str(age), "City": str(city)}
        print("Dictionary created, do you like to test it?")
        x = input()
        if x == "yes":
            for key, value in name.items():
                print(key + ":" + value)
        else:
            print("Thanks for trying the app")
        print("do you like to add another student?")
        x = input()
        if x == "yes":
            AddStudent()
        else:
            print("Thanks for trying the app")
    else:
        print("Thanks for trying the app")


print("do you like to add a student?")
x = input()
if x == "yes":
    AddStudent()
else:
    print("Thanks for trying the app")
