'''
2024-10-18
ogracias
topic = While loop
'''

# imports
import random

print('\n\n********************')
print('#1 while loop')
print('********************')
num = 0 # 1- declaring it and initializing variable
while(num < 5):# 2- test
    print('Hello')
    num += 1

print('\n\n********************')
print('#2 sentinel value')
print('********************')
num = int(input('Enter a number, -1 to stop: '))
while(num != -1):
    print('You entered: ' + str(num))
    num = int(input('Enter a number, -1 to stop: '))
print('Done')   



print('\n\n********************')
print('#3 Loops and strings')
print('********************')
name = input('Enter your name: ')
while name != 'Ada':
    print(name + ' is an interesting name.')
    name = input('Enter your name: ')
print('Cool, that is Ms. Lovelace\'s last name as well')
    

#===============================================================================
# Randomize 10 numbers from 1 - 10 inclusive using the
# while loop. Print each as the loop progresses
#===============================================================================
counter = 0
while(counter < 10):
    number = random.randint(1, 10)
    print('Number \u2192', number)
    counter += 1
    












