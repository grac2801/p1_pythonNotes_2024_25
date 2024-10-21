'''
2024-10-21
ogracias
title = count variables
'''

# imports

# print('\n\n*******************')
# print('#1- first counter of while loop')
# print('*******************')
# name = input('Enter a name: (STOP to end) ')
# counter = 0
#
# while(name != 'STOP'):
#     counter += 1
#     print('You entered: ' + name)
#     name = input('Enter a name: (STOP to end) ')
# print('You entered ' + str(counter) + ' name(s)')   
#
#
# print('\n\n*******************')
# print('#2- second counter for addition')
# print('*******************')
# num = int(input('Enter a number (-1 to stop): '))
# total = 0
#
# while(num != -1):
#     print('You entered: ' + str(num))
#     total += num
#     num = int(input('Enter a number (-1 to stop): '))
# print('the sum of the number is \u2192', total)


#===================================================================================================
# Student activity:
# write a program that will prompt the suer to enter a positive number.
# while they enter negative numbers, re-prompt them.
# Count how many times it takes until user inputs a positive value.
#==================================================================================================
n = int(input('Enter a positive number: '))
total = 1
while(n < 0):
    n = int(input('Enter a positive number: '))
    total += 1
print('That took you', total, 'tries.')   
   
    
    
    




