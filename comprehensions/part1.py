'''
Created on Feb 21, 2025

@author: ogracias
'''

if __name__ == '__main__':
    print('\n\n*******************')
    print('Comprehensions with numbers')
    print('*******************')
    nums = [1, 2, 3, 4, 5]
    print(nums)
    
    results = []
    def timesTwo(aList):
        for i in aList:
            i = i * 2
            results.append(i)
        return results
    nums2 = timesTwo(nums)
    print('nums2', nums2, sep='\u2192')
    
    #comprehensions
    nums3 = [i * 4 for i in nums] #iterable
    print(nums3)
    
    print('\n\n*******************')
    print('comprehensions and text')
    print('*******************')
    strings = ['welcome', 'to', 'computer', 'science']
    print(strings)
    
    results =[]
    for i in strings:
        i = i.upper()
        results.append(i)
    print('strings', results, sep='\u2192 ')
    
    # using a comprehension
    results2 = [i.upper() for i in strings]
    print('strings', results2, sep='\u2192 ')
    
    print('\n\n*******************')
    print('comprehensions and functions')
    print('*******************')
    def timesFive(num):
        return num * 5
    
    new_nums = [timesFive(i) for i in nums]
    print('new_nums', new_nums, sep='\u2192 ')
    
    
    print('\n\n*******************')
    print('if statements')
    print('*******************')
    nums = [1, 2, 3, 4, 5]
    def timesTen(num):
        num = num * 10
        return num
    
    answer = [timesTen(n) for n in nums if n > 2]
    print(answer)
    
    
    print('\n\n*******************')
    print('dictionaries and comprehensions')
    print('*******************')
    dicts = [{'name': 'Kai'}, {'name': 'Rayan'}]
    
    #algorithm
    results = []
    for i in dicts:
        results.append(i['name'])
    print('results', results, sep='\u2192')
    
    
    results2 = [i['name'] for i in dicts]
    print('results', results, sep='\u2192')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    