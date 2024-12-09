'''
2024-12-09
ogracias
title = Simple search
'''

# imports


# global variables | constants


# functions
def search(animals, value):
    indexFound = -1
    for i in range(len(animals)):
        if(animals[i] == value):
            indexFound = i
            return indexFound
    return indexFound
    
    

if __name__ == '__main__':
    words = ['cat', 'dog', 'mouse', 'lizard', 'bird']
    animal = input('What animal are you searching for? ')
    index = search(words, animal)
    print('The value appears at index position ' + str(index) + " [-1 means not found]")
    
    
    
    
    
    
    
    
    
    
    
    
    
