import random
import string
def passwd():
    passwd=""
    if strength == 1:
        for i in range(letters):
            passwd+=random.choice(string.ascii_lowercase)
        for i in range(digits):
            passwd+=random.choice(string.digits)
    elif strength == 2:
        for i in range(letters):
            passwd+=random.choice(string.ascii_letters)
        for i in range(digits):
            passwd+=random.choice(string.digits)
    elif strength == 3:
        for i in range(letters):
            passwd+=random.choice(string.ascii_letters+string.punctuation)
        for i in range(digits):
            passwd+=random.choice(string.digits)
    elif strength == 4:
        for i in range(length):
            passwd+=random.choice(string.ascii_letters+string.punctuation+string.digits)
    return passwd
def gen():
    password = passwd()
    return password
length = int(input("enter the total length of the password:"))
letters = int(input("enter the number of alphabets that to be present in the password:"))
digits = int(input("enter the number of digits that to be present in the password:"))
if length == letters+digits:
    strength = int(input("Please select the password difficulty\n"
                     "\t\t1.low\n"
                     "\t\t2.medium\n"
                     "\t\t3.high\n"
                     "\t\t4.secure\n"
                     "\t-->"))
    print("<-----------Generating Password------------->")
    print(gen())
else:
    exit()
