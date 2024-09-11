'''
Created on Sep 9, 2024

@author: ogracias
'''

print('Hello world')

# default separator
print('Hello', 'Mr.','Gracias')
print('Hello world')

# explicit separator
print('Hello', 'Mr.', 'Gracias', sep='&')
print('Hello', 'Mr.', 'Gracias', sep='\n')

firstNumber = 5
secondNumber = 10

print(firstNumber)
print(secondNumber)

print(firstNumber, end=' and ')
print(secondNumber)

# format
myAge = 53
favoriteColor = 'dark blue'
print('I am {0} years old, and my favorite color is {1}.'.format(myAge, favoriteColor))
print('I am {0} years old, and my favorite color is {1}.'.format(favoriteColor, myAge))
print('I am {1} years old, and my favorite color is {0}.'.format(favoriteColor, myAge))


#new formatting
print(f'I am {myAge} years old, and my favorite color is {favoriteColor}.')

print('\n\n********************')
print('concatenation')
print('********************')
print('Hello my friend' + 'Mary.')
print('5' + '11')
print(5 + 11)







