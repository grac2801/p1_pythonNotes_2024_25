'''
2025-02-03
ogracias
title = and or gates
'''

# imports


# global variables | constants
canVote = False

# functions
def voting(age):
    over18 = age
    if over18 > 18:
        canVote = True
        return canVote
    else:
        canVote = False
        return canVote

if __name__ == '__main__':
    #False
    print(bool(0))
    print(bool(1))
    print(bool(0j))
    
    # True
    print(bool(-1))
    print(bool(1j))
    
    
    #String
    print("Strings")
    print(bool('True'))
    print(bool('False'))
    print(bool(''))
    print(bool(' '))
    
    
    #Data structures
    print('\n\nData structures')
    print(bool([]))
    print(bool([1, 2]))
    
    
    print(bool(None))
    
    
    #Using logical operators
    myList = [1, 2, 3]
    if bool(myList):
        print('My list has some values')
        
        
    a = 5
    b = 5
    if(a -b):
        print('a and b are not equal')
        
    print(a == b)
    
    print('\n\n*******************')
    print('Logical gates')
    print('*******************')
    print('---OR gate---')
    print(False or False)
    print(False or True)
    print(True or False)
    print(True or True)
    
    print('\n\n*******************')
    print('AND gate')
    print('*******************')
    print(False and False)
    print(False and True)
    print(True and False)
    print(True and True)
    
    print('\n\n*******************')
    print('NOT gate')
    print('*******************')
    print(not False)
    print(not True)
    
    #example
    weatherIsNice = False
    haveUmbrella = True
    
    if not haveUmbrella or weatherIsNice:
        print('stay inside')
    else:
        print('Go for a walk')
        
    print("Example 2 --> DeMorgan's law")  
    
    weatherIsNice = True
    haveUmbrella = False
    
    if not(haveUmbrella or weatherIsNice):
        print('stay inside')
    else:
        print('Go for a walk')
    "============================================="
    if(not haveUmbrella) and (not weatherIsNice):
        print('Stay inside')
    else:
        print('Go for a walk')
        
    
    
    
    
    print(voting(5))
    
    
    
    
    
    
    
    
    
    
    
    

