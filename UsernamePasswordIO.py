
usernameList = ["test1", "test2"]
passwordList = ["test1", "test2"]
passwordBlackList = [",", "_", "[", "]", ";", "'", '"',"/", "=", "+", "-", ".", "!", "@"]

# Validates that all characters in user inputted Password do not match any in the black list
def validatePassword(inputPass):
    passwordBlackList = [",", "_", "[", "]", ";", "'", '"', "/", "=", "+", "-", ".", "!", "@"]
    if any(char in passwordBlackList for char in inputPass):
        return False
    return True

# Creates a new Username
def NewUser():
    newUser = (input("Please enter a new username: "))
    usernameList.append(newUser)

# Creates a new Password
def NewPass():
    passMessage = "Please enter a new password: "
    inputPass = input(passMessage)
    while validatePassword(inputPass) == False:
        passMessage = "ERROR: Please do not include illegal characters (, . _ etc)"
        inputPass = input(passMessage)

    else:
        newPass = inputPass
        passwordList.append(newPass)

# Username Verification
def verifyUsername():
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
def verifyPassword(userNumber):
    correctPassword = passwordList[userNumber]
    inputPassword = ""
    passMessage = "Please enter your password: "

    while correctPassword != inputPassword:
        inputPassword = (input(passMessage))
        passMessage = "ERROR: Password is incorrect!, Please re-try: "

    if correctPassword == inputPassword:
        print("Welcome, %s!" % usernameList[userNumber])

# Creation
NewUser()
NewPass()
# Verification
userNumber = verifyUsername()
verifyPassword(userNumber)
