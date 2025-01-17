'''
2025-01-15
ogracias
title = title
'''

# imports


# global variables | constants


# functions
def count_evens(nums):
    counterEvens = 0
    for i in nums:
        if i % 2 == 0:
            counterEvens += 1
    return counterEvens

def big_diff(nums):
    if len(nums) >= 1:
        highest = max(nums)
        lowest = min(nums)
        diff = highest - lowest
    return diff


def sum13(nums):
    s = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 1
        else:
            s += nums[i]
            
        i += 1
        
    return s


if __name__ == '__main__':
    
    print(count_evens([2, 1, 2, 3, 4]))
    print(count_evens([2, 2, 0]))
    print(count_evens([1, 3, 5]))
    
    print(big_diff([10, 3, 5, 6]))
    print(big_diff([7, 2, 10, 9]))
    print(big_diff([2, 10, 7, 2]))

    
    

