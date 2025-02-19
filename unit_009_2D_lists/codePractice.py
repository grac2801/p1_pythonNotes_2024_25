'''
Created on Feb 19, 2025

@author: ogracias
'''


def printList(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()


def swapValues(a):
    temp = []  # empty list that we will append to
    for i in range(len(a)):
    # add from end to beginning of original list
        temp.append(a[len(a) - 1 - i])
    return temp


# Traveling back means keeping the items in the lists, but flipping the order in each list
def flipOrder(a):
    temp = a
    for i in range(len(a)):
        temp[i] = swapValues(a[i])  # assign each reversed list to the new list
    printList(temp)


'''MAIN'''
MrGList = [["Miami" , "Atlanta", "Dallas", "Los Angeles"], ["New York", "Chicago", "Portland", "Sacramento"]]

printList(MrGList)
print()  # blank space
flipOrder(MrGList)
