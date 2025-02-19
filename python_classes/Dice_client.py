'''
2025-02-19
ogracias
title = client
'''

# imports
from python_classes.Dice import Dice

# global variables | constants


# functions


if __name__ == '__main__':
    kelly = Dice('Kelly')
    jaden = Dice('Jaden')
    print()
    kelly.tossDice()
    kelly.printDice()
    
    print()
    jaden.tossDice()
    jaden.printDice()
    
    kelly.compareScores(jaden)
