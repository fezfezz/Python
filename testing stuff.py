
usernameList = []
passwordList = ["rikimaru"]

# Username
newUser = (input("Please enter your username: "))
usernameList.append(newUser)
userNumber = usernameList.index(newUser)

# Password
correctPassword = passwordList[userNumber]
inputPassword = ""
passMessage = "Please enter your password: "
while correctPassword != inputPassword:
    inputPassword = (input(passMessage))
    passMessage = "ERROR: Password is incorrect!, Please re-try: "

if (correctPassword == inputPassword):
    print("Password is correct!")
