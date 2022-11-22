"""Welcome to the code of BoBi Sprache. This Sprache aka Language will 
put the letter "bi" after each vocal letter in your name"""

print("Welcome to the BoBiSprache programm")
username = input("Please enter your name to be BoBied :D : ")
vowels = ["a", "e", "i", "o", "u"]


def VowelCheck(name):
    bobified_name = ""
    for i in name:
        bobified_name += i
        if i in vowels:
            bobified_name += "bi"
    return bobified_name


print("Your New Name is: %s" % VowelCheck(username).title())
