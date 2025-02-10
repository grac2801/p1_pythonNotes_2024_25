

# imports


# global variables | constants


# functions

    




if __name__ == '__main__':
    pw = input('Enter password: ')
    pw = list(pw)
    for letter in range(len(pw)):
        if(pw[letter] == 'a'):
            pw[letter] = pw[letter].replace("a", "e")
        elif(pw[letter] == 'e'):
            pw[letter] = pw[letter].replace("e", "i")

    print(pw)

   

   