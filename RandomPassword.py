import random
import string

def passwordGenerator():
    password = random.randint(10,24)
    passwordArray = []
    separator = ""
    symbols = ["-", "|", "@",".",",","?","/","!","~","#","%","^","&","*","(",")","{","}","[","]","=","*"]
    for x in range(password):
        randSpecialChar = random.randint(0,21);
        passwordArray.append(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + symbols[randSpecialChar]))
    return str(separator.join(passwordArray))

def passwordVerifier():
    upperFlag = 0
    lowerFlag = 0
    specialCharFlag = 0
    numberFlag = 0
    while (numberFlag == 0 or upperFlag == 0 or lowerFlag == 0 or specialCharFlag == 0):
        password = passwordGenerator()
        for x in range(0,len(password)):
            if (password[x].isdigit() == 1):
                numberFlag = 1
            if (password[x].isupper() == 1):
                upperFlag = 1
            if (password[x].islower() == 1):
                lowerFlag = 1
            if (password[x].isalnum() == 0):
                specialCharFlag = 1
    print(password)
passwordVerifier()
