'''
2024-10-25
ogracias
topic = continue - break
'''

# imports
from time import sleep

print('\n\n********************')
print('#1 rocket taking off')
print('********************')
countdown = 3
while(countdown > 0):
    print(countdown)
    # sleep(1)
    countdown -= 1
    if(countdown == 0):
        print('Take off!!!')
        # sleep(2)
        break
print('Good luck explorers')



print('\n\n********************')
print('#2 - continue')
print('********************')
startFloor = 8
while(startFloor < 16):
    if(startFloor == 13):
        startFloor += 1
        continue
    print(f'current floor: {startFloor} Going to next')
    sleep(1)
    startFloor += 1
else:
    print('You have reached the top of the building!')
    
print('\n\n********************')
print('#3- trace and display output')
print('********************')
x = 0
while(x < 11):
    if(x == 7):
        
        sleep(1)
        continue
    elif(x == 9):
        print('You hit 9. Now breaking!')
        seconds = 3
        while(seconds > 0):
            print(seconds, ' to break')
            sleep(1)
            seconds -= 1
        x += 1
        break
    else:
        print(x)
        sleep(1)
        x += 1
print('No problems')
    
    
    
    
    
    
    
    
    
    
    
    
    

        
    










