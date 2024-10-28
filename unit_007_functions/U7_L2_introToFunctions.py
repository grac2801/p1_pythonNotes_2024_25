'''
2024-10-28
ogracias
topic = 7-2 intro to functions
'''


# imports
from random import randint

def add():
    firstNum = float(input('Enter a number: '))
    secondNum = float(input('Enter another number: '))
    total = firstNum + secondNum
    print('The result is', total)
    
def flipCoin():
    outcome = randint(0, 1)
    if outcome == 1:
        print('heads')
    else:
        print('tails')
    
if __name__ == '__main__':
    add()









