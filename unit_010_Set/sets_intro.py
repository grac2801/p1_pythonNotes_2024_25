'''
2025-01-24
ogracias
title = sets intro
'''

# imports


# global variables | constants


# functions


if __name__ == '__main__':
    print('\n\n*******************')
    print('start an empty set')
    print('*******************')
    emptySet = set()
    print(emptySet)
    
    even_numbers = {2, 4, 6, 8}
    print(even_numbers)
    
    print('\n\n*******************')
    print('unique values')
    print('*******************')
    letters = set('letters')
    print(letters)
    print(len(letters))
    
    print('\n\n*******************')
    print('list into a set')
    print('*******************')
    reindeers_list = ['Dasher', 'Dancer', 'Dancer', 'Prancer']
    reindeers_set = set(reindeers_list)
    print(reindeers_set)
    
    print('\n\n*******************')
    print('make a set from a tuple')
    print('*******************')
    sea_animals_tuple = ('dolphin','whale', 'whale', 'fish')
    sea_animal_set = set(sea_animals_tuple)
    print(sea_animal_set)
    
    print('\n\n*******************')
    print('when using dictionaries, only keys are visible')
    print('*******************')
    fruits_dict = {
                'apple'  : 'red',
                'orange' : 'orange',
                'pear'   : 'green',
                'banana' : 'yellow'
        }
    fruits_set = set(fruits_dict)
    print(fruits_set)
    
    animals = {
        'bipedal'  : {'humans', 'kangaroo'},
        'carnivore': {'lion', 'pig'},
        'omnivore' : {'humans', 'pig', 'chimpanzee'},
        'herbivore': {'pig', 'cow', 'deer', 'humans'},
        'quadrupedal': {'dog', 'lion'},
        'smart'    : {'humans', 'whales', 'chimpanzee'}
        }
    print(animals)
    
    print('\n\n*******************')
    print('which types have humans in them')
    print('*******************')
    counter = 0
    for types, creatures in animals.items():
        if 'humans' in creatures:
            counter += 1
            print(counter, '-', types)
    
    print('\n\n*******************')
    print('which type(s) have humans and either chimpanzee or kangaroo')
    print('*******************')
    for types, creatures in animals.items():
        if 'humans' in creatures and ('kangaroo' in creatures or 'chimpanzee' in creatures):
            print(types)
    
    
    print('\n\n*******************')
    print('find which type(s) have humans but not kangaroos')
    print('*******************')
    for types, creatures in animals.items():
        if('humans' in creatures and ('kangaroo' not in creatures)):
            print(types)
    
    #===============================================================================================
    # These following algorithms involve methods from the set class
    #===============================================================================================
    
    print('\n\n*******************')
    print('which animals have human and chimpanzee? [& means intersection]')
    print('*******************')
    for types, creatures in animals.items():
        if creatures & {'chimpanzee'} and creatures & {'humans'}:
            print(types)
    for types, creatures in animals.items():
        if creatures.intersection('chimpanzee') and creatures.intersection('humans'):
            print(types)
    
    
    print('\n\n*******************')
    print('which animals have humans, but neither chimpanzee nor pig')
    print('*******************')
    for types, creatures in animals.items():
        if 'humans' in creatures and not creatures & {'chimpanzee', 'pig'}:
            print(types)
    
    
    print('\n\n*******************')
    print('set operator')
    print('*******************')
    set_a = {1, 2}
    set_b = {2, 3}
    print(set_a & set_b)
    
    
    
    print('\n\n*******************')
    print('union or | ')
    print('*******************')
    set_a = {1, 2}
    set_b = {2, 3}
    print(set_a | set_b)
    print(set_a.union(set_b))
    
    
    print('\n\n*******************')
    print('difference or -')
    print('*******************')
    set_a = {1, 2}
    set_b = {2, 3}
    print(set_a - set_b)
    print(set_a.difference(set_b))
    
    
    print('\n\n*******************')
    print('symmetric difference of ^')
    print('*******************')
    #Items in one set or the other, but not both
    print(set_a ^ set_b)
    print(set_a.symmetric_difference(set_b))
    
    print('\n\n*******************')
    print('issubset() or <=')
    print('*******************')
    set_a = {1, 2}
    set_b = {1, 2, 3}
    print('Is set_a a subset of b?', set_a.issubset(set_b))
    print('Is set_a a subset of b?', set_a <= set_b)
    
    print('\n\n*******************')
    print('issuperset() or >=')
    print('*******************')
    set_a = {1, 2}
    set_b = {1, 2, 3}
    print('Is set_a a superset of b?', set_a.issuperset(set_b))
    print('Is set_a b superset of a?', set_b >= set_a)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
