'''
2024-10-23
ogracias
topic = for loops
'''

# imports
import random

print('\n\n********************')
print('#1 review of while')
print('********************')
'''
You need 3 things: 
1-declare and initialize
2-test (T or F)
3-change the variable
'''
count = 1
while(count < 6):
    print(str(count) + ' : Hello')
    count += 1

print('\n\n********************')
print('#2- syntax of a for loop')
print('********************')
for each in range(5):
    print('Hello')

print('\n\n********************')
print('#3- range(start, stop)')
print('********************')
for i in range(1, 11):
    print(i, end=" ")

print('\n\n********************')
print('#4- range(start, stop, step)')
print('********************')
n = int(input('How many iterations? '))
for i in range(2, n + 1, 2):
    print(i)


print('\n\n********************')
print('#5- range(start, stop, step)')
print('********************')
for i in range(100, 0, -10):
    print(i)

#===============================================================================
# student activity:
# simulate the toss of 2 coins three times.
# state how many times the same sides were observed
# print you answer
#===============================================================================
same_side_counter = 0
n = int(input('How many coin tosses? '))
for i in range(1, n + 1):
    print('toss # ' + str(i))
    coin1 = random.randint(0, 1)
    print('coin1:', coin1)
    coin2 = random.randint(0, 1)
    print('coin2:', coin2)
    print()

    if(coin1 == coin2):
        same_side_counter += 1

print('Coins were the same side', same_side_counter, ' times.')

print('\n\n********************')
print('#6- iterating through a string')
print('********************')
country = 'United States of America'
for letter in country:
    if letter.isupper():
        print(letter)

#===============================================================================
# student activity:
# iterate through a string and write a new
# string by changing only the 'a' letters into
# the symbol \u2192 (-->)
#===============================================================================
orig_phrase = 'Today is a great day. Don\'t you think?'
new_phrase = ''
orig_letter = 'a'
new_letter = '\u2192'
total_a = 0

for i in orig_phrase:
    if(i == orig_letter):
        new_phrase += new_letter
        total_a += 1
    else:
        new_phrase += i

print('original phrase:', orig_phrase)
print('new phrase:', new_phrase)
print('total A found:', total_a)















