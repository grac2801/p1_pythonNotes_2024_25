'''
2024-09-162024-09-13
ogracias
title = Special formatting
'''

# imports


print('*******************')
print('data type in print f')
print('*******************')
'''
s --> String
d --> integer, uses comma as a separator
e --> exponent
f --> fixed point notation. Default is 6 [float]
'''
variable = 1045634
print(f'Using numeric {variable}')
print(f'Using numeric {variable = }')
print(f'Using numeric {variable:d}')
print(f'Using numeric {variable:10}')
print(f'Using numeric {variable:e}')

print('*******************')
print('float variables')
print('*******************')
pi = 3.141592653589793
print(f'Using the value of pi = {pi}')
print(f'|{pi:<25}|')
print(f'|{pi:>25}|')
print(f'|{pi:^25}|')
print(f'|{pi:25}|')


print('*******************')
print('float formatting')
print('*******************')
floatVariable = 1_045_634.664646546;
print(f'This prints w/out formatting {floatVariable = }')
print(f'This prints w/out formatting {floatVariable}')
print(f'This prints w/out formatting {floatVariable:f}')
print(f'This prints w/out formatting {floatVariable:,f}')
print(f'This prints w/out formatting {floatVariable:,.2f}')
print(f'This prints w/out formatting {floatVariable:+,.2f}')



print('*******************')
print('String formatting')
print('*******************')
version = 'Python 3.12'
print(f'|{version:25}|')
print(f'|{version:<25}|')
print(f'|{version:>25}|')
print(f'|{version:^25}|')


print('*******************')
print('tabbing')
print('*******************')
fish = 'Salmon'
first ='Monday'
second = 'Tuesday'
third = 'Wednesday'
meal1 = fish
meal2 = 'soup'
meal3 = 'beef'
print(f'|{first:10s}{second:10s}{third:10s}|')
print(f'|{meal1:10s}{meal2:10s}{meal3:10s}|')















