'''
Created on Jan 17, 2025

@author: ogracias
'''
# modes: r for reading, w for writing, a for appending, 
# x = for writing
# with open("myFriends.txt", 'r') as f:
    # contents = f.readline()
    # print(contents, end ="")
    # contents = f.readline()
    # print(contents)
    
    # read a specific amount of characters
    # charactersToRead = 10
    # content = f.read(charactersToRead)
    # print(content)
    
    #for loop
    # for line in f:
    #     print(line, end='')
    
    #while loop
    # sizeToRead = 10
    # contents = f.read(sizeToRead)
    # while len(contents) > 0:
    #     print(contents, end = '*')
    #     contents = f.read(sizeToRead)
    
    #reading file into a list
    # readlines()
    # myArray = []
    # myArray = f.readlines()
    # print(myArray)
    
    #remove new line character \n
    # myArray = list()
    # contents = f.readlines()
    # for line in range(len(contents)):
    #     line = contents[line].strip('\n')
    #     myArray.append(line)
    # print(myArray)
    
 
try:   
    with open("myNewFile.txt", 'x') as f:
        f.write("This is my line 1\n")
        f.write("This is my line 2\n")
        f.write("This is my line 3\n\n")
except FileExistsError:
    print('File already exits')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        








