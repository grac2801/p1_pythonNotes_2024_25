'''
2024-10-11
ogracias
topic = elif
'''

# imports

myComment = '''
pH level           category
0 - 4              Strong acid
5 - 6              weak acid
7                  Neutral or pure water
8 - 9              weak base
10 - 14            Strong base
'''
print(myComment)

print('\n\n********************')
print('Match to the correct description of pH')
print('********************')
value = float(input('Enter the pH level: '))
if value > 0:
    if value < 7.0:
        print('It is acidic')
        print('You should be careful with that!')
    elif value > 7.0 and value <= 14:
        print('It is basic')
    elif value == 7:
        print('it is neutral')
elif value > -10:
    print('You input a negative pH value')
else:
    print('less than 10')       
print('Done')        


















