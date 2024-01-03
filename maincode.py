import random
import time


def generator(lines):
    for line in lines:
        yield line


print("Welcome to the password generator!")
while True:
    try:
        length = int(input(("How long do you want the password: ")))
    except ValueError:
        print("Enter a number")
    else:
        if length > 15:
            print("Password too long")
            continue
        else:
            break
print("Choose one from below:\n")
time.sleep(0.5)

passGen = "abcdefghijklmnoprsqtuvxyzw1234567890!*/-+="
passLetters = ""
i = 1 
i2 = 1
passwords = []
while True:
    if i >= 10:
        break
    passLetters += random.choice(passGen)
    if i2 == length:
        passwords.append(passLetters)
        passLetters = ""
        i2 = 0
        i += 1
    i2 += 1


gen = generator(passwords)
stopline = len(passwords)
i = 1
while i <= stopline:
    print(next(gen))
    i += 1
print()
