'''
2024-10-28
ogracias
topic = testing
'''

# imports


import unit_007_functions.U7_L2_introToFunctions as calc
import unit_007_functions.calculator_parameters as calcp
import unit_007_functions.calculator_return as calcr

if __name__ == '__main__':
    calc.add()
    calcp.add(5, 1)
    myparameter1 = float(input('Enter a first parameter: '))
    myparameter2 = float(input('Enter a second parameter: '))
    calcp.add(myparameter1, myparameter2)
    result = calcr.add(5, 9)
    print(result)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    