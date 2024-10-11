'''
2024-10-11
ogracias
topic = simple ifs
'''

# imports




print('\n\n********************')
print('simple if')
print('********************')
value = int(input('Enter a number: '))
if value > 0:
    print('Positive!')
print('Done')




print('\n\n********************')
print('Another if statement')
print('********************')
sunny = True
if sunny:
    print('I do not need an umbrella')
if not sunny:
    print('I DO need an umbrella')




print('\n\n********************')
print('odd or even')
print('********************')
number = int(input('Enter a number: '))
if number % 2 == 0:
    print(str(number) + ' is even')
if number % 2 == 1:
    print(str(number) + ' is odd')


print('\n\n********************')
print('syntax is grammar for coding')
print('********************')
word = input('Enter the secret word: ')
if word ==  'python':
    print('correct!')


#===============================================================================
# Student activity:
# ask the user for a number and check whether
# it is positive, negative, or zero.
# print completed when done
# Only use if not else statements
#===============================================================================
value = int(input('Enter a number: '))
if value == 0:
    print('zero')
if value > 0:
    print(str(value) + ' is > 0')
if value < 0:
    print(str(value) + ' is < 0')
print('Completed.')










