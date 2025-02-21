'''
Created on Feb 21, 2025

@author: ogracias
'''
from random import randint
import math

if __name__ == '__main__':
    myList = [1, 2, 3, 4, 5]
    example = [i for i in myList]
    print('example', example, sep='\u2192 ')
    
    example2 = [i * 5 if i == 3 else i for i in myList]
    print('example2', example2, sep='\u2192 ')
    
    example3 = [i for i in myList if i > 3]
    print('example3', example3, sep='\u2192 ')
    
    example4 = [i * 5 if i == 3 else i for i in myList if i > 3]
    print('example4', example4, sep='\u2192 ')
    
    
    finalList = list()
    for value in range(5):
        finalList.append(randint(1, 10))
    print('finalList', finalList, sep='\u2192 ')
        
    
    squaredList = [int(math.pow(i, 2)) for i in finalList]
    print('squaredList', squaredList, sep='\u2192 ')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    