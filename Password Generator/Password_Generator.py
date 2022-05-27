import random

# value store in variable from input
web_name = list(input("Name of the Sites : "))
types = list(input("Type of the Sites : "))
cap_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small_alpha = cap_alpha.lower()
years = list(input("Enter Opening Year: "))
unique = list(input("unique alpha: ").lower())
unique_digit = list(input("unique digit: "))
purpose = list(input("purpose : "))
layer = list(input('Blocking layer : '))

# use as variable to randomly select small or capital letter
checker = [cap_alpha,small_alpha]

# list for containing all password
main_password = list()

# function for checking capital or not
def iscap(test):
    if test >= 'A' and test <= 'Z':
        return True
    return False


# checking each letter of the website name and convert to small.
for name in web_name:
    if iscap(name) == True:
        main_password.append(name.lower())


# checking each letter of the website type and convert to small.
for type in types:
    if iscap(type) == True:
        main_password.append(type.lower())



doubicapte_finder = list()

# common function for website name and website category
def website():
    [i, checkA, checkB, checkE, checkF, checkI, checkM, checkS, checkW] = [0,0,0,0,0,0,0,0,0]

    for check in main_password:
        if check == "a" and checkA == 0:
            x = main_password.pop(i)
            doubicapte_finder.append(x)
            main_password.insert(i,"@")
            checkA = 1

        elif check == "b" and checkB == 0:
            x = main_password.pop(i)
            doubicapte_finder.append(x)
            main_password.insert(i,"&")
            checkB = 1

        elif check == "e"  and checkE == 0:
            x = main_password.pop(i)
            doubicapte_finder.append(x)
            main_password.insert(i,"#")
            checkE = 1

        elif check == "f"  and checkF == 0:
            x = main_password.pop(i)
            doubicapte_finder.append(x)
            main_password.insert(i,"£")
            checkF = 1

        elif check == "i"  and checkI == 0:
            x = main_password.pop(i)
            doubicapte_finder.append(x)
            main_password.insert(i,"!")
            checkI = 1

        elif check == "m"  and checkM == 0:
            x = main_password.pop(i)
            doubicapte_finder.append(x)
            main_password.insert(i,"w")
            checkM = 1

        elif check == "s"  and checkS == 0:
            x = main_password.pop(i)
            doubicapte_finder.append(x)
            main_password.insert(i,"$")
            checkS = 1
        
        elif check == "w"  and checkW == 0:
            x = main_password.pop(i)
            doubicapte_finder.append(x)
            main_password.insert(i,"m")
            checkM = 1

        else:
            pass

        i += 1
        

# calling website
website()

# function for number check of years
def is_num(test):
    if test >= 0 and test <= 9:
        return True
    return False

# adding years to your password
for num in years:
    if is_num(int(num)) == True:
        main_password.append(num)


# function for unique alphabet
def unique_alpha():
    [checkA, checkI, checkN]= [0,0,0]

    for letter in unique:
        if letter not in doubicapte_finder:
            if letter == "i" and checkI == 0:
                doubicapte_finder.append(letter.lower())
                main_password.append("!")
                checkI = 1
            elif letter == "a" and checkA == 0:
                doubicapte_finder.append(letter.lower())
                main_password.append("@")
                checkA = 1
            elif letter == "n" and checkN == 0:
                doubicapte_finder.append(letter.lower())
                main_password.append("u")
                checkN = 1
            else:
                doubicapte_finder.append(letter.lower())
                main_password.append(letter.lower())
        else:
            doubicapte_finder.append(letter.lower())
            main_password.append(letter.lower())


# call unique alphabet
unique_alpha()

# Function for Unique Digit 
def unique_digits():
    for digit in unique_digit:
        main_password.append(digit)


# calling unique digit
unique_digits()

# function for purpose in alpha
def purpose_alpha():
    checkA,checkI = (0,0)
    checkN = 0
    for letter in purpose:
        if iscap(letter) == True:
            if letter not in doubicapte_finder:
                if letter == "i" and checkI == 0:
                    doubicapte_finder.append(letter.lower())
                    main_password.append("!")
                    checkI = 1
                elif letter == "a" and checkA == 0:
                    doubicapte_finder.append(letter.lower())
                    main_password.append("@")
                    checkA = 1
                elif letter == "n" and checkN == 0:
                    doubicapte_finder.append(letter.lower())
                    main_password.append("u")
                    checkN = 1
                else:
                    doubicapte_finder.append(letter.lower())
                    main_password.append(letter.lower())
            else:
                doubicapte_finder.append(letter.lower())
                main_password.append(letter.lower())


# calling purpose_alpha function
purpose_alpha()

# deleting the doubicapte_finder list
del doubicapte_finder

def block_layer_one():
    # function for random choices
    def keyword(value):
        return random.choice(value)

    # for the upper case in the first letter
    try:
        up_alpha = main_password[0].upper()
        main_password.pop(0)
        main_password.insert(0,up_alpha)

    except:
        pass


    # adding an extra random alphabet at first to your password make it more strong.
    while(True):
        value = keyword(keyword(checker))
        if value not in main_password:
            main_password.insert(0,value)
            break

    # adding an extra random alphabet at last to your password make it more strong.
    while(True):
        value = keyword(keyword(checker))
        leng = len(main_password)
        if value not in main_password:
            main_password.insert(leng,value)
            break

def block_layer_two():
    # checking each letter of the layer.
    count = 0

    for letter in reversed(layer):
        if iscap(letter) == True and count%2 == 0:
            # adding an extra random alphabet at first to your password make it more strong.
            main_password.insert(0,letter)
        elif iscap(letter) == True and count%2 == 1:
            # adding an extra random alphabet at last to your password make it more strong.
            main_password.insert(len(main_password),letter)
        count = count + 1

# function for calling block
def block():
    if len(layer) == None or len(layer) == 0:
        block_layer_one()
    else:
        block_layer_two()

# call block
block()

# final password
print(f'\nPassword : [ {"".join(main_password)} ]')