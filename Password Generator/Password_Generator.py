import random

# value store in variable from input
web_name = list(input("Name of the Sites : "))
types = list(input("Type of the Sites : "))
cap_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small_alpha = cap_alpha.lower()
unique = list(input("unique alpha: ").lower())
unique_digit = list(input("unique digit: ").lower())
purpose = list(input("purpose : "))


checker = [cap_alpha,small_alpha]

# list for containing all password
lis = list()

# function for checking capital or not
def iscap(test):
    if test > 'A' and test < 'Z':
        return True
    return False


# checking each letter of the website name and convert to small.
for name in web_name:
    if iscap(name) == True:
        lis.append(name.lower())


# checking each letter of the website type and convert to small.
for type in types:
    if iscap(type) == True:
        lis.append(type.lower())



lis2 = list()

# common function for website name and website category
def website():
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
        

# calling website
website()

# copying all data from lis2 to lis3
lis3 = lis2.copy()

# function for unique alphabet
def unique_alpha():
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


# call unique alphabet
unique_alpha()

# deleting the list lis2
del lis2

# Function for Unique Digit 
def unique_digits():
    for digit in unique_digit:
        lis.append(digit)


# calling unique digit
unique_digits()

# creating list 4 for pu
lis4 = list()
for pur in purpose:
    if iscap(pur) == True:
        lis4.append(pur.lower())


# function for purpose in alpha
def purpose_alpha():
    checkA,checkI = (0,0)
    checkN = 0
    for letter in lis4:
        if letter not in lis3:
            if letter == "i" and checkI == 0:
                lis3.append(letter)
                lis.append("!")
                checkI = 1
            elif letter == "a" and checkA == 0:
                lis3.append(letter)
                lis.append("@")
                checkA = 1
            elif letter == "n" and checkN == 0:
                lis3.append(letter)
                lis.append("u")
                checkN = 1
            else:
                lis3.append(letter)
                lis.append(letter)
        else:
            lis3.append(letter)
            lis.append(letter)


# calling purpose_alpha function
purpose_alpha()

# copying all data to password
password = lis

# deleting the lists
del lis,lis3,lis4

# for the upper case in the first letter
try:
    x = password[0].upper()
    password.pop(0)
    password.insert(0,x)

except:
    pass

# function for random choices
def keyword(values):
    return random.choice(values)


# adding an extra random alphabet at first to your password make it more strong.
while(True):
    value = keyword(keyword(checker))
    if value not in password:
        password.insert(0,value)
        break

# adding an extra random alphabet at last to your password make it more strong.
while(True):
    value = keyword(keyword(checker))
    leng = len(password)
    if value not in password:
        password.insert(leng,value)
        break

print(f'Password : [ {"".join(password)} ]')