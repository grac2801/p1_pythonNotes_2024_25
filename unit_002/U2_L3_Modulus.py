'''
2024-09-16
ogracias
title = Modulus or remainder, mod
'''

# imports
#===================================================================================================
# mod is used for remainder, patterns, even or odd, cybersecurity
#===================================================================================================
print('When 10 is divided by 3, the remainder is', 10 % 3)

print(23 % 7)

#===================================================================================================
# When the first value < second value, then the answer is the first value
#===================================================================================================
firstValue = int(input('Enter first value: '))
secondValue = int(input('Enter second value: '))
print(firstValue % secondValue)



print('*******************')
print('Another example')
print('*******************')
seconds = int(input('How many seconds are you converting? '))
minutes = int(seconds / 60)
secondsLeft = int(seconds % 60)
print(f'There are {minutes:d} minutes(s) and {secondsLeft:d} second(s) left')