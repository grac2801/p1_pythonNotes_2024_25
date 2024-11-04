'''
2024-10-30
ogracias
topic = scope
'''

# imports
from random import randint


# functions
def guessNumber():
    global total
    guess = int(input('Enter a number \u2192 '))# local variable
    total += 1
    test(guess)
    

def test(num):
    global total
    if num > rand:
        print('Your guess is too high.')
        guessNumber()
    elif num < rand:
        print('Your guess is too low.')
        guessNumber()
    else:
        print('You guess the right numbers')
        print('It only took you', total, 'times')
        

if __name__ == '__main__':
    rand = randint(1, 100)# global variable
    print(rand)
    total = 0
    guessNumber()










