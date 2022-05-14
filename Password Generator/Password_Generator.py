import random

names = list(input("Name of the Sites : "))
types = list(input("Type of the Sites : "))
cap_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small_alpha = cap_alpha.lower()
unique = list(input("unique alpha: ").lower())
unique_digit = list(input("unique digit: ").lower())
purpose = list(input("purpose : "))
checker = [cap_alpha,small_alpha]


lis = list()
def iscap(test):
    if test > 'A' and test < 'Z':
        return True

for name in names:
    if iscap(name) == True:
        lis.append(name.lower())


for type in types:
    if iscap(type) == True:
        lis.append(type.lower())

lis2 = list()
def first():
    [i, checkA, checkB, checkE, checkF, checkI, checkM, checkS, checkW] = [0,0,0,0,0,0,0,0,0]

    for check in lis:

        if check == "a" and checkA == 0:
            x = lis.pop(i)
            lis2.append(x)
            lis.insert(i,"@")
            checkA = 1

        elif check == "b" and checkB == 0:
            x = lis.pop(i)
            lis2.append(x)
            lis.insert(i,"&")
            checkB = 1

        elif check == "e"  and checkE == 0:
            x = lis.pop(i)
            lis2.append(x)
            lis.insert(i,"#")
            checkE = 1

        elif check == "f"  and checkF == 0:
            x = lis.pop(i)
            lis2.append(x)
            lis.insert(i,"£")
            checkF = 1

        elif check == "i"  and checkI == 0:
            x = lis.pop(i)
            lis2.append(x)
            lis.insert(i,"!")
            checkI = 1

        elif check == "m"  and checkM == 0:
            x = lis.pop(i)
            lis2.append(x)
            lis.insert(i,"w")
            checkM = 1

        elif check == "s"  and checkS == 0:
            x = lis.pop(i)
            lis2.append(x)
            lis.insert(i,"$")
            checkS = 1
        
        elif check == "w"  and checkW == 0:
            x = lis.pop(i)
            lis2.append(x)
            lis.insert(i,"m")
            checkM = 1

        else:
            pass

        i += 1
        

first()

lis3 = lis2.copy()

def uniqucy():
    [checkA, checkI, checkN]= [0,0,0]

    for letter in unique:
        if letter not in lis2:
            if letter == "i" and checkI == 0:
                lis3.append('I')
                lis.append("!")
                checkI = 1
            elif letter == "a" and checkA == 0:
                lis3.append(letter.upper())
                lis.append("@")
                checkA = 1
            elif letter == "n" and checkN == 0:
                lis3.append(letter.upper())
                lis.append("u")
                checkN = 1
            else:
                lis3.append(letter.upper())
                lis.append(letter.lower())
        else:
            lis3.append(letter.upper())
            lis.append(letter.lower())

uniqucy()

# number
def uniqucy_dig():
    [checkA, checkI, checkN]= [0,0,0]

    for digit in unique_digit:
        if digit not in lis2:
            if digit == "3" and checkI == 0:
                lis.append('9')
                checkI = 1
            elif digit == "7" and checkA == 0:
                lis.append("8")
                checkA = 1
            elif digit == "9" and checkN == 0:
                lis.append("3")
                checkN = 1
            else:
                lis.append('7')


uniqucy_dig()

lis4 = list()
for pur in purpose:
    if iscap(pur) == True:
        lis4.append(pur)


def purposy():
    checkA,checkI = (0,0)
    checkN = 0
    for letter in lis4:
        if letter not in lis3:
            if letter == "I" and checkI == 0:
                lis3.append('I')
                lis.append("!")
                checkI = 1
            elif letter == "A" and checkA == 0:
                lis3.append(letter.upper())
                lis.append("@")
                checkA = 1
            elif letter == "N" and checkN == 0:
                lis3.append(letter.upper())
                lis.append("u")
                checkN = 1
            else:
                lis3.append(letter.upper())
                lis.append(letter.lower())
        else:
            lis3.append(letter.upper())
            lis.append(letter.lower())

purposy()

password = lis

try:
    x = password[0].upper()
    password.pop(0)
    password.insert(0,x)

except:
    pass

def keyword(values):
    return random.choice(values)


while(True):
    value = keyword(keyword(checker))
    if value not in password:
        password.insert(0,value)
        break


while(True):
    value = keyword(keyword(checker))
    leng = len(password)
    if value not in password:
        password.insert(leng,value)
        break

print(f'Password : [ {"".join(password)} ]')