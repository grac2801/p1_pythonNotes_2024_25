'''
2024-11-13
ogracias
title = strings
'''

# imports


# global variables | constants


# functions
def _1_capitalize(fn, ln):
    '''
    It capitalizes both first and last names for the customer
    str --> str
    example: oscAR --> Oscar
    '''
    capitalized_fn = fn.capitalize()
    capitalized_ln = ln.capitalize()
    return capitalized_fn + ' ' + capitalized_ln

if __name__ == '__main__':
    # strings are immutable
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    print(_1_capitalize(first, last))

    
