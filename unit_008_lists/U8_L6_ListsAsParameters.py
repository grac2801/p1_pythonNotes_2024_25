'''
2024-12-04
ogracias
title = title
'''

# imports


# global variables | constants


# functions
def change(a):
    a += 1
    print(a)


def changeArray(a):
    for i in range(len(a)):
        a[i] += 1


def changePositions(position1, position2, colorsArray):
    temp = colorsArray[position1 - 1]
    colorsArray[position1 - 1] = colorsArray[position2 - 1]
    colorsArray[position2 - 1] = temp
    
    
if __name__ == '__main__':
    # passing by value. It applies to simple values
    x = 0
    print(x)
    change(x)
    print(x)


    # Passing objects | Passing a reference
    x = [0, 1, 2, 3]
    print(x)
    changeArray(x)
    print(x)
    
    # swapping values
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    print(colors)
    choice1 = int(input('Enter the first element you want to switch \u2192 '))
    choice2 = int(input('Enter the second element you want to switch \u2192 '))
    changePositions(choice1, choice2, colors)
    print(colors)
    
    
    
    
    
    
    
    
    
    
    
    
    
    