'''
2024-11-04
ogracias
title = Nested loops
'''

# imports


# global variables | constants


# functions


if __name__ == '__main__':
    print('\n\n*******************')
    print('1- Basic nested loop syntax')
    print('*******************')
    for outer in range(1, 4):
        print('outer:', outer)
        for inner in range(4, 7):
            print('inner:', inner, end='  ')
        print()
    
    
    print('\n\n*******************')
    print('better formatted loop')
    print('*******************')
    for outer in range(1, 4):
        print('outer:', outer, end= ' | ')
        for inner in range(4, 7):
            print('inner:', inner, end=' | ')
        print()
    
    
    print('\n\n*******************')
    print('compounds | elements')
    print('*******************')
    alkali_metals = ['Li', 'Na', 'K']
    halogens = ['F', 'Cl']
    for metal in alkali_metals:
        print('iteration', metal)
        for halogen in halogens:
            print(metal + halogen)
        print()
    
    
    print('\n\n*******************')
    print('rows and columns')
    print('*******************')
    rows = int(input('How many rows? '))
    cols = int(input('How many cols? '))
    for letter in range(rows):
        for j in range(cols):
            print('* ', end = '')
        print()
    
    
    #===============================================================================
    # pyramids
    #===============================================================================
    print("\n\n")
    print('-------- topic 3 = bottom left --------')
    bottom_left = '''
    print the image below with 5 rows
    * 
    * * 
    * * * 
    * * * * 
    * * * * *
    '''
    for letter in range(6):
        for j in range(letter):
            print(f'{"*":2}', end="")
        print()
        
    
    
    print("\n\n")
    print('-------- topic 4 = upper left --------')
    upper_left = '''
    print the image below with 5 rows
    * * * * * 
    * * * * 
    * * * 
    * * 
    *
    '''
    # print(upper_left)
    for letter in range(5, 0, -1):
        for j in range(letter, 0, -1):
            print(f'{"*":2}', end='')
        print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
