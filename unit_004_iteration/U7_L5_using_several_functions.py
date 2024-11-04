'''
2024-10-30
ogracias
title = using several functions
'''

# imports
from random import randint

#functions
def guessNumber():
    global total
    guess = int(input('Enter a number \u2192 '))
    total += 1
    test(guess)
    
def test(num):
    #print(guess) error since not in scope
    global total
    if num > rand:
        print('Your guess is too high!\n')
        guessNumber()
    elif num < rand:
        print('Your guess is too low.\n')
        guessNumber()
    else:
        print('You guess the right number.')
        print('it took you', total, 'guesses')
        


if __name__ == '__main__':
    rand = randint(1, 100)
    print(rand)
    total = 0
    guessNumber()
    