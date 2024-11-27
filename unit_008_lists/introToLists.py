'''
2024-11-18
ogracias
title = Intro to lists
'''


# imports
import random

# global variables | constants


# functions
def removeLastItemInList(L):
    '''
    (list) --> (list)
    Remove last item in list
    removeLastItemInList([2, 3, 4]) --> [2, 3]
    '''
    del L[-1]
    return L
    

def removeUsingPop(passedList):
    '''
    (list) --> (list)
    Remove last item using pop() method
    removeUsingPop([2, 3, 4]) --> [2, 3]
    '''
    passedList.pop()
    return passedList
    


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
    
    print('\n\n*******************')
    print('insertion')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    marxes.insert(0, 'first')
    print(marxes)
    
    
    print('\n\n*******************')
    print('deletion')
    print('*******************')
    # delete the first item added before
    del marxes[0]
    print(marxes)
    
    
    #delete Hunter
    marxes.remove('Hunter')
    print(marxes)
    
    
    print('\n\n*******************')
    print('pop()')
    print('*******************')
    # It allows you to remove an item knowing its index
    marxes.pop() # last item
    print(marxes)
    marxes.pop(0) # delete first item
    print(marxes)
    
    
    print('\n\n*******************')
    print('index()')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    print(marxes.index("Chico"))
    
    
    # search for whether an item is found in a list without searching for index
    is_here = 'Mario' in marxes
    print(is_here)
    
    
    print('\n\n*******************')
    print('join()')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    print(', '.join(marxes))
    
    friends = ['Harry', 'Hermione', 'Ron']
    print(friends)
    separator =  ' & '
    
    friends_joined = separator.join(friends)
    print(friends_joined)
    
    
    print('\n\n*******************')
    print('sort')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    sorted_marxes = sorted(marxes) # makes a copy and sorts it.
    print(sorted_marxes)
    print('original marxes', marxes)
    
    # sort marxes but do not make a copy. Sort in place
    marxes.sort(reverse=True)
    print(marxes)
    
    
    print('\n\n*******************')
    print('Make a function using a list')
    print('*******************')
    numbers = [2, 1, 4.0, 3, 7]
    print(numbers)
    print(removeLastItemInList(numbers))

    a = [1, 2, 3]
    print('a =', a)
    b = a[:]
    print('b =', b)
    
    a[0] = 1000
    print('a =', a)
    
    c = list()
    c.append(123)
    print(c)
    
    d = list()
    d += [12, 24, 36]
    print(d)
    
    e = []
    e.extend(d)
    print(d)
    print(e)
    
    
    print('\n\n*******************')
    print('using another function')
    print('*******************')
    listToSendToFx = ['Joe', 'Marge', 'Steph', 'Lily']
    print(listToSendToFx)
    print(removeUsingPop(listToSendToFx))
    
    
    
    print('\n\n*******************')
    print('min and max')
    print('*******************')
    myNumbers = [4, -2, 6, -7, 0, 8.2, -3.1]
    print(min(myNumbers))
    print(max(myNumbers))
    
    
    
    
    
