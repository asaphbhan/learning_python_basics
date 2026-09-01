#here I will create a encryption program
capital=["A",'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def find_letter(letter,casing):
    match casing:
        case 'c':
            return(capital.index(letter))

        case 's':
            return(small.index(letter))

def even_cipher(letter): #all even place alphabets are shifted forward by two places
    return_letter='a'
    if letter in capital:
        casing='c'
        if letter=='Y':
            return_letter="A"
        elif letter=='Z':
            return_letter="B"
        else:
            return_letter=capital[find_letter(letter,casing)+2]

    elif letter in small:
        casing='s'
        if letter=='y':
            return_letter="a"
        elif letter=='z':
            return_letter="b"
        else:
            return_letter=small[find_letter(letter,casing)+2]
    return return_letter

def even_decrypt(letter):
    return_letter='a'
    if letter in capital:
        casing='c'
        if letter=='A':
            return_letter="Y"
        elif letter=='B':
            return_letter="Z"
        else:
            return_letter=capital[find_letter(letter,casing)-2]

    elif letter in small:
        casing='s'
        if letter=='a':
            return_letter="y"
        elif letter=='b':
            return_letter="z"
        else:
            return_letter=small[find_letter(letter,casing)-2]
    return return_letter

def odd_cipher(letter): #all odd places alphabets are moved back by one place
    return_letter='a'
    if letter in capital:
        casing = 'c'
        if letter == 'A':
            return_letter = "Z"
        else:
            return_letter = capital[find_letter(letter, casing)-1]

    elif letter in small:
        casing = 's'
        if letter == 'a':
            return_letter = "z"
        else:
            return_letter = small[find_letter(letter, casing)-1]
    return return_letter

def odd_decrypt(letter):
    return_letter='a'
    if letter in capital:
        casing = 'c'
        if letter == 'Z':
            return_letter = "A"
        else:
            return_letter = capital[find_letter(letter, casing)+1]

    elif letter in small:
        casing = 's'
        if letter == 'z':
            return_letter = "a"
        else:
            return_letter = small[find_letter(letter, casing)+1]
    return return_letter

def encryption(string):
    result=[]
    position=0 #the cipher counts the places 'including spaces'
    for letter in string:
        if letter== " ": #checks the spaces and adds them as it is
            result.append(' ')
        elif letter not in capital and letter not in small: #all special characters and numbers are added as they are
            result.append(letter)
        else:
            if position%2==0: #positive positions are ciphered separate and so are odd ones
                result.append(even_cipher(letter))
            elif position%2!=0:
                result.append(odd_cipher(letter))
        position+=1
    return ''.join(result)

def decryption(string): #use this to decrypt the ciphered text
    result=[]
    position=0
    for letter in string:
        if letter== " ":
            result.append(' ')
        elif letter not in capital and letter not in small:
            result.append(letter)
        else:
            if position%2==0:
                result.append(even_decrypt(letter))
            elif position%2!=0:
                result.append(odd_decrypt(letter))
        position+=1
    return ''.join(result)

choice=1
while choice!=3:
    choice=int(input("What would you like to do?\n1.Encrypt your message\n2.Decrypt your message\n3.Exit\n:"))
    while choice not in [1,2,3]:
        choice=int(input("Please enter a valid input: "))
    if choice=='3':
        break
    text_in = input("Please enter your message: ")

    match choice:
        case 1:
            print(encryption(text_in))
        case 2:
            print(decryption(text_in))