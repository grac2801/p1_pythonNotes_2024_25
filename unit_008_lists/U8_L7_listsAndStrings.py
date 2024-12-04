'''
2024-12-04
ogracias
title = lists and strings
'''

# imports


# global variables | constants


# functions


if __name__ == '__main__':
    # Strings are lists with index values
    month = 'October'
    for i in range(len(month)):
        print(month[i])
        
        
        
    # You can also replace values in the array, but you have to use
    # an index value
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print('original weekdays:', weekdays)
    for i in range(len(weekdays)):
        weekdays[i] = weekdays[i].replace("day", "")
    print('modified weekdays:', weekdays)
    
    
    
    # parallel processing or parallel lists (Have to be of same length)
    name = ['Alice', 'Bob', 'Carl']
    color = ['blue', 'orange', 'red']
    age = [16, 15, 17]
    for i in range(len(name)):
        print(name[i] + ' is ' + str(age[i]) + ' years old')
        print('His/her favorite color is ' + color[i])
    
    
    # zip() function
    names = ['John', 'Alice', 'Bob', 'Lucy']
    scores = [89, 92, 99, 90]
    result = zip(names, scores)
    print(list(result))
    
    
    
    
    
    
