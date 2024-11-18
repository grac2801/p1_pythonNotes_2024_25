'''
2024-11-18
ogracias
title = Intro to lists
'''
<<<<<<< HEAD
=======
from pip._vendor.chardet.latin1prober import OTH
>>>>>>> 7d3604793c1d2243ca1d92f3a70762f8e3ee2a9c

# imports
import random

# global variables | constants


# functions


if __name__ == '__main__':
    print('\n\n*******************')
    print('1. create a list')
    print('*******************')
    # Empty list
    myList = []
    print(myList)
    other_list = list()
    print('other_list', other_list)
    
    values = list()
    print(values) #start
    for i in range(10):
        myRandomNum = random.randint(1, 10)
        values.append(myRandomNum)
    print(values)#end
    
    
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu']
    print(weekdays)
    
    big_birds = ['emu', 'ostrich', 'cassowary']
    first_names = ['Sebastian', 'Tyler', 'Vivian']
    combined = [weekdays, big_birds, first_names]
    print('combined:', combined)
    print(combined[1])
    only_cassowary = combined[1][2]
    print(only_cassowary)
    
    
    print('\n\n*******************')
    print('offsets | slices')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    #print first item
    print(marxes[0])
    #print all but last one
    print(marxes[0:4]) # first is inclusive, last value is exclusive
    # print all except first one
    print(marxes[1:5])
    # print only the last one
    print(marxes[-2])
    
    
    print('\n\n*******************')
    print('change items in list')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    marxes[2] = 'Eric'
    print(marxes)
    
    #going backwards
    #[start, end, step]
    print(marxes[::])
    print(marxes[::-1])
    print(marxes[::2])
    
    
    print('\n\n*******************')
    print('append and extend')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    marxes.append('Raphael')
    print(marxes)
    extended_values = ['David', 'Kelly']
    marxes.extend(extended_values)
    print(marxes)
    
    
    
    
    print('\n\n*******************')
    print('+=')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    others = ['Theresa', 'Andres']
    marxes += others
    print(marxes)
    # += and extend add each value to your list
    
    
    
    
    
    
    
    
    
