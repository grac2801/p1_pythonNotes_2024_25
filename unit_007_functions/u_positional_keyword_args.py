'''
2024-11-04
ogracias
title = keyword positional args
'''

# imports


# global variables | constants
# constants ALWAYS have to be capitalized.
DAYS_OF_THE_WEEK = 7
STARTING_SALARY = 100_000
print(f'Starting salary: ${STARTING_SALARY:,.2F}')
# print speed of light in m/s 3 x 10 ^8
print(f'The speed of light is {3e8:,.2f} m/s')


# functions
def menu(drink, entree, dessert):
    print(f'drink: {drink}, entree: {entree}, and dessert: {dessert}')
    
def menuWithItems(drink, entree = 'Chicken', dessert = 'Pie'):
    print(f'drink: {drink}, entree: {entree}, and dessert: {dessert}')

def menuWithItemsAllIncluded(drink = 'Tea', entree = 'Chicken', dessert = 'Pie'):
    print(f'drink: {drink}, entree: {entree}, and dessert: {dessert}')





if __name__ == '__main__':
    menu('Sprite', 'Spaghetti', 'Cheesecake')
    
    beverage, meal, sweets = 'tea', 'steak', 'chocolate cake'
    menu(beverage, meal, sweets)
    menuWithItems(drink = 'Sprite', entree = 'Spaghetti')
    menuWithItems('7Up')
    menuWithItems(drink = 'Orange Fanta', entree = 'Steak', dessert = 'Flan')
    menuWithItemsAllIncluded()
    menuWithItemsAllIncluded(dessert = 'Ice cream')
