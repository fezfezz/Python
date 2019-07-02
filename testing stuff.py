
usernameList = []
passwordList = ["rikimaru"]


def NewUser():
    newUser = (input("Please enter a new username: "))
    usernameList.append(newUser)

# Creation
NewUser()

# Username
inputUser = ""
userMessage = "Please enter your username: "
while inputUser not in usernameList:
    inputUser = input(userMessage)
    userMessage = "ERROR: Username cannot be found, Please re-try: "
if inputUser in usernameList:
    userNumber = usernameList.index(inputUser)

# Password
correctPassword = passwordList[userNumber]
inputPassword = ""
passMessage = "Please enter your password: "

while correctPassword != inputPassword:
    inputPassword = (input(passMessage))
    passMessage = "ERROR: Password is incorrect!, Please re-try: "

if correctPassword == inputPassword:
    print("Welcome, %s!" % usernameList[userNumber])
