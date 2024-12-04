'''
2024-11-06
ogracias
title = Function documentation
'''

# imports


# global variables | constants


# functions
def SelectOnly_d(word) -> int:
    '''
    Returns number of letter d found in the word parameter
    String --> int
    SelectOnly_d('day of the dead') --> 3
    '''
    count = 0
    for letter in word:
        if letter == 'd':
            count += 1
    return count

if __name__ == '__main__':
    total_d = SelectOnly_d("Day of the dead")
    print(f'The total number of d letters \u2192 {total_d}')
    
    
    total :int = 6
