'''
2024-12-09
ogracias
title = Intro to dictionaries
'''

# imports


# global variables | constants


# functions


if __name__ == '__main__':
    print('\n\n*******************')
    print('1. Declare a dictionary | Remove last item [popitem()]')
    print('*******************')
    capitals = {"UK": "London", 'France': 'Paris', 'Germany': 'Berlin'}
    print(capitals)
    returned_value = capitals.popitem()
    print(returned_value)
    print(capitals)
    
    
    print('\n\n*******************')
    print('2. copy key into a variable, and print')
    print('*******************')
    UK_cap = capitals['UK']
    print(UK_cap, len(UK_cap))
    
    print('\n\n*******************')
    print('3. Add items to dictionary')
    print('*******************')
    print(capitals)
    capitals['USA'] = 'Washington DC'
    print(capitals)
    
    
    print('\n\n*******************')
    print('4. print all keys in dictionary')
    print('*******************')
    capitals = {"UK": "London", 'France': 'Paris', 'Germany': 'Berlin'}
    returned_keys = capitals.keys()
    print(returned_keys)
    # Make keys into a list #5
    returned_keys_list = list(capitals.keys())
    print('list: ', returned_keys_list)
    
    
    
    print('\n\n*******************')
    print('6. get values from dictionary')
    print('*******************')
    returned_capitals = capitals.values()
    print(returned_capitals)
    
    for i in capitals.values():
        print(i)



    print('\n\n*******************')
    print('7. Make values into a list')
    print('*******************')
    returned_values_list = list(capitals.values())
    print(returned_values_list)
    
    
    print('\n\n*******************')
    print('8. popitem() raises keyerror')
    print('*******************')
    capitals = {'Mexico': "Mexico city"}
    print(capitals)
    returned_mexico = capitals.popitem()
    print(capitals)
    
    # returned_mexico = capitals.popitem()
    # print(capitals)
    
    print('\n\n*******************')
    print('9. Try clause')
    print('*******************')
    capitals = {"UK": "London", 'France': 'Paris', 'Germany': 'Berlin'}
    try:
        print(capitals['UK'])
        print(capitals['Germany'])
        print(capitals['Spain'])
    except KeyError:
        print('Country not in dictionary')
        
        
    print('\n\n*******************')
    print('10. get()')
    print('*******************')
    print(capitals)
    print(capitals.get('UK'))
    print(capitals.get('Germany'))
    print(capitals.get('Spain', 'not in dictionary'))
    
    print('\n\n*******************')
    print('11. items()')
    print('*******************')
    print(capitals)
    print(capitals.items())
    #make items into a list
    print(list(capitals.items()))
    
    
    
    print('\n\n*******************')
    print('12. update a dictionary')
    print('*******************')
    print(capitals)
    more_capitals = {'Spain': 'Madrid', 'Italy': 'Rome'}
    capitals.update(more_capitals)
    print(capitals)
    
    
    print('\n\n*******************')
    print('13. Copying a dictionary')
    print('*******************')
    car = {
        'brand': 'Ford',
        'model': 'Mustang',
        'year' : 1964
        }
    copied_car = car.copy()
    print(car)
    print(copied_car)
    
    
    print('\n\n*******************')
    print('14. populate a dictionary')
    print('*******************')
    good_students = {
        'Jason': 100,
        'Mary' : 98,
        'Luisa': 100
        }
    print(good_students)
    
    students = ['John', 'Johnie', 'Juan']
    bad_grade = 0
    bad_students = dict.fromkeys(students, bad_grade)
    print(bad_students)
    
    
    print('\n\n*******************')
    print('pop()')
    print('*******************')
    car = {
        'brand': 'Ford',
        'model': 'Mustang',
        'year' : 1964
        }
    print(car)
    #remove 'Mustang'
    car.pop('model') 
    print(car)
    
    print('\n\n*******************')
    print('16. setdefault()')
    print('*******************')
    car = {
        'brand': 'Ford',
        'model': 'Mustang',
        'year' : 1964
        }
    car.setdefault('tire model', '4XTRWZ')
    print(car)
    
    
    
    #fromkeys
    fruits = ['Apple', 'Pear', 'Peach', 'Banana']
    fruit_dictionary = dict.fromkeys(fruits, 'in stock')
    # fruits['Pear'] = 9.89
    # print(fruit_dictionary)
    
    print('\n\n*******************')
    print('zip()')
    print('*******************')
    pants = ['jeans', 'casual', 'dress']
    prices = [45.00, 63.50, 89.25]
    pants_dict = dict(zip(pants, prices))
    print(pants_dict)