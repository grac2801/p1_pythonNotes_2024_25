'''
2024-10-09
ogracias
topic = randomizer
'''

# imports
import random
#===============================================================================
# random gives a value >= 0 but less than 1
#===============================================================================
print(random.random())

print("value from dice", random.randint(1, 6))
print(f'value from dice is {random.randint(1, 6)}')


# alternative value between 1 and 6
# * = number of values
# + = where to start
print(int(random.random() * 6) + 1)

print(random.choice(["Joseph", "Isabel", 'Lori', 'Michael']))

#===============================================================================
# activity:
# write a program to generate a unique password
# include a number from 1 to 100
# an animal 
# another number between 1 and 10
# example --> 45Moose3
#===============================================================================
num1 = random.randint(1, 100)
animal = random.choice(['elephant', 'cat', 'dog'])
num2 = random.randint(1, 10)
print('The password is ' + str(num1) + animal + str(num2))
