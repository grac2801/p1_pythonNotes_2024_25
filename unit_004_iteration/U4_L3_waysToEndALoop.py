'''
2024-10-21
ogracias
title = Ways to end a loop
'''

# imports
# print('\n\n*******************')
# print('#1- counter or user input')
# print('*******************')
# count = 1
# while(count <= 10): #count is set to only 10 times
#     print(f'{count:4}: Python')
#     count += 1
#
#
# print('\n\n*******************')
# print('#2- Ask user for 5 numbers & add number divisible by 3')
# print('*******************')
# counter  = 0
# totalSum = 0
# while(counter < 5):
#     n = int(input('Enter a number: '))
#     if(n % 3 == 0):
#         print(str(n) + ' is divisible by 3.')
#         totalSum += n
#     counter += 1
# print('The total sum of %3 == 0: ', totalSum)


#===================================================================================================
# student activity:
# Ask user to input numbers. sentinel -1 to end.
# Provide the average of all numbers input to 2 numbers passed the decimal point.
#===================================================================================================
counter = 0
addition = 0
n = int(input('Enter a number (-1 to end)'))
if n == -1:
    print('-1 input. Script ends')
else:
    while(n != -1):
        counter += 1
        addition += n
        n = int(input('Enter a number (-1 to end)'))
    average = (addition / counter)
    print(f'The average is {average:,.2f}')
    print('Done')
    









