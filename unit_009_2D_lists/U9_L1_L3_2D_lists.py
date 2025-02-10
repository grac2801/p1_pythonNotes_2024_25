'''
2025-02-10
ogracias
title = Intro to 2D arrays
'''

# imports


# global variables | constants


# functions


if __name__ == '__main__':
    newGrades = [[9, 8, 7, 8],
                 [8, 7, 10, 9],
                 [5, 7, 3, 9]
                ]
    for row in newGrades:
        for col in row:
            print(f"{col:^3}{'|':1}", end='')
        print()
    
    #===============================================================================================
    # How many A's did they get (A = 9 or 10)
    #===============================================================================================
    count = 0
    for row in newGrades:
        for col in row:
            if col >= 9:
                count += 1
    print(f'The class got {count} A grades in the exam\n\n')
    
    
    #===============================================================================================
    # Let's change all 8s to 2s 
    #===============================================================================================
    for row in range(len(newGrades)):
        for col in range(len(newGrades[row])):
            if(newGrades[row][col] == 8):
                newGrades[row][col] = 2
                
    #now print it
    for row in range(len(newGrades)):
        for col in range(len(newGrades[row])):
            print(f'{newGrades[row][col]:5}', end='')
        print()
    
                
    print('\n\n*******************')
    print('appending values')
    print('*******************')
    grades = []
    grades.append([89, 88, 90])      
    grades.append([92, 99, 79])      
    grades.append([100, 98, 96])
    print(grades)
    for row in grades:
        for col in row:
            print(f'{col:^4}{"|"}', end='')
        print('\n\n')
    
    grades[1][1] = 100
    for row in grades:
        for col in row:
            print(f'{col:^4}{"|"}', end='')
        print()
    
    names = [['Bob', 'Alice', 'Carl'],
             ['Joe', 'Jim', 'Sue'],
             ['Kelly', 'Joshua', 'Andres']
            ]
    
    print(names)
    moreNames = ['stu1', 'stu2', 'stu3']
    names[2].append(moreNames)
    print(names)
    
    #===============================================================================================
    # STUDENT ACTIVITY = Increase each grade by 1 & print
    #===============================================================================================
    grades2 = [[9, 8, 7, 8],
            [8, 7, 6, 8],
            [5, 9, 7, 9]
        ]
    
    for row in range(len(grades2)):
        for col in range(len(grades2[row])):
            grades2[row][col] += 1
   
    print("print it")
    for r in grades2:
        for c in r:
            print(c, end='\t')
        print()
    
    
    