'''
2024-10-09
ogracias
title = builtins
'''

#imports
import math
import platform
from math import sqrt
#===============================================================================
# min and max 
#===============================================================================
myList  = [4, 5, 2, 9, 23, -3, -2]
print(min(myList))
print(max(myList))
print(ord('A'))


names = ['Stephanie', 'John', 'Audrey', 'Julia' ]
print(min(names))
print(max(names))

print('\n\n********************')
print('builtins using input')
print('********************')
# a = int(input('Enter a first number: '))
# b = int(input('Enter a second number: '))
# c = int(input('Enter a third number: '))
# print('Biggest value: '+ str(max(a, b, c)))


print('\n\n********************')
print('student activity')
print('********************')
#===============================================================================
# anotherList = [4, 6, 2, 78, 23, 56, 12]
# print the difference between the highest and lowest
# values of the list
# use the f formatting for it
#===============================================================================
anotherList = [4, 6, 2, 78, 23, 56, 12]
print(f'The difference is {max(anotherList) - min(anotherList)}')


#===============================================================================
# square root of 81
#===============================================================================
print(int(81**(1/2)))
print(int(math.sqrt(81)))
print(int(math.pow(81, (1/2))))
print(math.fabs(56.32))
print(math.ceil(math.fabs(56.32)))
print(math.floor(math.fabs(56.32)))


print('My current Python version ' + platform.python_version())
print('My current processor is', platform.processor())
print('My system is', platform.system())
print('My system is', platform.version())


print(sqrt(7))
