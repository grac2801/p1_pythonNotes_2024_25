'''
2025-01-17
ogracias
title = tuples introduction
'''

# imports


# global variables | constants


# functions


if __name__ == '__main__':
    fact = 'tuples are immutable [can not be changed]'
    
    print('\n\n*******************')
    print('1. empty tuple')
    print('*******************')
    empty_tuple = ()
    print(empty_tuple)
    
    
    print('\n\n*******************')
    print('2. making tuples')
    print('*******************')
    friends = ('Rob', 'Nancy', 'Esther')
    print('friends:', friends)
    
    
    #You don't need parenthesis
    animals = 'dog', 'lion', 'fish'
    print('animals', animals)
    print(type(animals))
    
    print('\n\n*******************')
    print('2a. Single item in tuple')
    print('*******************')
    myTuple = 5,
    print(myTuple)
    
    
    print('\n\n*******************')
    print('3.assign multiple values to multiple variables')
    print('*******************')
    trees = ('cedar', 'oak', 'lemon')
    a, b, c = trees
    print('a', a)
    print('b', b)
    print('c', c)
    
    
    print('\n\n*******************')
    print('4.Easily swap values')
    print('*******************')
    a = 1
    b = 2
    
    #normally
    temp = a
    a = b
    b = temp
    
    #for tuples
    password = 'swordfish'
    ice_cream = 'chocolate'
    
    print('password =', password, ', ice cream =', ice_cream)
    password, ice_cream = 'chocolate', 'swordfish'
    print('password =', password, ', ice cream =', ice_cream)
    
    print('\n\n*******************')
    print('5. tuple function')
    print('*******************')
    my_list = ['one', 'two', 'three']
    print(my_list)
    my_tuple = tuple(my_list)
    print(my_tuple)
    
    #===============================================================================================
    # tuples vs lists
    # a) tuples use less memory
    # b) can not change tuples by error
    # c) you can use tuples as keys in a dictionary
    # d) can be passes as parameters in functions
    #===============================================================================================
    print(my_tuple.index("two"))
    
    # my_tuple.append("four") --> can not be changed.
    
    print('\n\n*******************')
    print('6. for loops and tuples')
    print('*******************')
    myTuple = ('Ram', 23, 10, 'Stephanie', 17, 'Alexa')
    myElement = 23
    for t in myTuple:
        if t == myElement:
            print('index of given element', myElement, 'is', myTuple.index(t))
            
            
    print('\n\n*******************')
    print('7.for loops and [i]')
    print('*******************')
    for i in range(len(myTuple)):
        print(i, myTuple[i])
        
        
    print('\n\n*******************')
    print('8. they can vary in size')
    print('*******************')
    # student_list = []
    # numStudents = int(input('How many students? '))
    #
    # for i in range(numStudents):
    #     fn = input('first name: ')
    #     ln = input('last name: ')
    #     idNum = int(input('id number: '))
    #     student_tuple = (fn, ln, idNum)
    #     student_list.append(student_tuple)
    #     print('\n\n')
    # print(student_list)
    
    
    
    
    print('\n\n*******************')
    print('9.tuple to list')
    print('*******************')
    hobbies_tuple = 'fishing', 'soccer', 'basketball'
    print('hobbies', hobbies_tuple)
    
    hobbies_list = list(hobbies_tuple)  
    print('hobbies list', hobbies_list)
    
    print('\n\n*******************')
    print('10. tuple to dictionary')
    print('*******************')
    tuple_fn = 'John', 'Mary', 'Francis'
    tuple_ln = 'Cooper', 'Armstrong', 'Pedroza'
    tuple_to_list = list(zip(tuple_fn, tuple_ln))
    print(tuple_to_list)
        
    print('\n\n*******************')
    print('11. tuples in indices')
    print('*******************')
    tuple_cities = 'San Jose', 'San Diego', 'San Francisco'
    print('The second city is:', tuple_cities[1])
    
    
    
    
    
    
    
    
    
    
    
