"""Welcome to the code of BoBi Sprache. This Sprache aka Language will 
put the letter "bi" after each vocal letter in your name"""

print("Welcome to the BoBiSprache programm")
Name = input("Please enter your name to be BoBied :D : ")
NameList = list(Name.lower())

vocals = ["a", "e", "i", "o", "u"]


def VocalCheck(NameList):
    for i in NameList:
        index = NameList.index(i)
        for j in vocals:
            if i == j and (str(NameList[index - 1]) + str(NameList[index])) != "bi":
                NameList.insert(index + 1, "bi")


VocalCheck(NameList)
NewName = ""
NewName = (NewName.join(NameList)).title()
print("Your New Name is: %s" % NewName)
