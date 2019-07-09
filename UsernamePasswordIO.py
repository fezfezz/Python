import sys
import csv
import PySimpleGUI as sg
from collections import defaultdict


usernameList = ["jeff", "meme"]
passwordList = ["jeff", "meme"]
passwordBlackList = [",", "@", "[", "]", ";", "'", '"', "/", "=", "+", "-", ".", "!", "^", "%", "#", "?", "{", "}", "*", "(", ")", "`", "~", " ", "null", ""]
resettingPassword = False


def main():
    readFile()
    writeFile()
    selectMessage = "\n" + "Please select an option:" + "\n" + "1: Sign Up" + "\n" + "2: Log In" + "\n" + "3: Reset Password" + "\n" + "4: Exit"
    selection = input(selectMessage)
    while selection != "4":
        if selection == "1":
            NewUser()
            NewPass()
            print("New user %s registered!" % usernameList[-1])
            main()
        elif selection == "2":
            userNumber = VerifyUsername()
            if (VerifyPassword(userNumber) == True):
                print("Welcome, %s!" % usernameList[userNumber])
            main()
        elif selection == "3":
            resetPassword()
            main()
        selectMessage = "Please select a valid option"
        selection = input(selectMessage)
    else:
        sys.exit()


# Validates that all characters in user inputted Password do not match any in the black list
def ValidatePassword(inputPass):
    if any(char in passwordBlackList for char in inputPass):
        return False
    return True


# Validates that no other user is currently called the same name
def ValidateUsername(inputUser):
    for name in usernameList:
        if name == inputUser:
            return False
    return True


# Creates a new Username
def NewUser():
    inputUser = (input("Please enter a new username: "))
    while ValidateUsername(inputUser) == False:
        userMessage = "ERROR: Username is already taken!" + "\n" + "Please enter a new username"
        inputUser = input(userMessage)
    newUser = inputUser
    usernameList.append(newUser)


# Creates a new Password
def NewPass():
    global resettingPassword
    passMessage = "Please enter a new password: "
    if resettingPassword == True: passMessage = "Please enter a NEW password: "
    inputPass = input(passMessage)
    while ValidatePassword(inputPass) == False:
        passMessage = "ERROR: Please do not include any blank spaces or special symbols (, . _ @ etc)"
        inputPass = input(passMessage)

    if resettingPassword == True:
        newPass = inputPass
        return newPass

    else:
        newPass = inputPass
        passwordList.append(newPass)


# Username Verification
def VerifyUsername():
    inputUser = "null"
    userMessage = "Please enter your username: "
    while inputUser not in usernameList:
        inputUser = input(userMessage)
        userMessage = "ERROR: Username cannot be found, Please re-try: "

    if inputUser in usernameList:
        userNumber = usernameList.index(inputUser)
        print("Username found!")
        return userNumber


# Password Verification
def VerifyPassword(userNumber):
    correctPassword = passwordList[userNumber]
    inputPassword = "null"
    passMessage = "Please enter your password: "
    if resettingPassword == True:
        passMessage = "Please enter your OLD password: "

    while inputPassword != correctPassword:
        inputPassword = (input(passMessage))
        passMessage = "ERROR: Password is incorrect!, Please re-try: "

    if inputPassword == correctPassword:
        return True


# Resets password using Verify() and New() functions
def resetPassword():
    global resettingPassword
    userNumber = VerifyUsername()
    resettingPassword = True
    if VerifyPassword(userNumber) == True:
        newPass = NewPass()
    del passwordList[userNumber]
    passwordList.insert(userNumber, newPass)
    resettingPassword = False


# this is completely fucked, reading normally just splits everything into rows, so it is useless
# the fix to this is to probably just read the file, convert to a string, split the string into list
def readFile():
    global usernameList
    global passwordList
    # Username reading
    with open("usernames.csv", 'rb') as usernameFile:
        reader = csv.reader(usernameFile, delimiter=' ', quotechar='|')
        for row in reader:
            print(', '.join(row))


# Username and Password saving
def writeFile():
    global usernameList
    global passwordList

    # Username writing
    with open("usernames.csv", 'w', newline='') as usernameFile:
        wr = csv.writer(usernameFile, quoting=csv.QUOTE_ALL)
        wr.writerow(usernameList)

    # Password writing
    with open("passwords.csv", 'w', newline='') as passwordFile:
        wr = csv.writer(passwordFile, quoting=csv.QUOTE_ALL)
        wr.writerow(passwordList)


main()


