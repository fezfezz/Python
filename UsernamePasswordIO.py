import sys


usernameList = ["test1", "test2", "fez"]
passwordList = ["test1", "test2", "eskettit"]
passwordBlackList = [",", "_", "[", "]", ";", "'", '"',"/", "=", "+", "-", ".", "!", "@"]


def main():
    selectMessage = "\n" + "Please select an option:" + "\n" + "1: Sign Up" + "\n" + "2: Log In" + "\n" + "3: Exit"
    selection = input(selectMessage)
    while selection != "3":
        if selection == "1":
            NewUser()
            NewPass()
            main()
        elif selection == "2":
            userNumber = VerifyUsername()
            VerifyPassword(userNumber)
            main()
        selectMessage = "Please select a valid option"
        selection = input(selectMessage)
    else:
        sys.exit()


# Validates that all characters in user inputted Password do not match any in the black list
def ValidatePassword(inputPass):
    passwordBlackList = [",", "_", "[", "]", ";", "'", '"', "/", "=", "+", "-", ".", "!", "@"]
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
    passMessage = "Please enter a new password: "
    inputPass = input(passMessage)
    while ValidatePassword(inputPass) == False:
        passMessage = "ERROR: Please do not include illegal characters (, . _ etc)"
        inputPass = input(passMessage)

    else:
        newPass = inputPass
        passwordList.append(newPass)


# Username Verification
def VerifyUsername():
    inputUser = ""
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
    inputPassword = ""
    passMessage = "Please enter your password: "

    while correctPassword != inputPassword:
        inputPassword = (input(passMessage))
        passMessage = "ERROR: Password is incorrect!, Please re-try: "

    if correctPassword == inputPassword:
        print("Welcome, %s!" % usernameList[userNumber])


if __name__ == "__main__": main()



