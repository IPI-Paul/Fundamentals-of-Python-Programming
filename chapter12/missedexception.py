# Listing 12.8
# Is a slight modification of Listing 12.6 to illustrate an unhandled exception
# Author: Rick Halterman
# Last modified: 

import random

for i in range(10):     # Loop 10 times
    print('Beginning of loop iteration', i)
    try:
        r = random.randint(1, 4)    # r is pseudorandomly 1, 2, 3, or 4
        if r == 1:
            print(int('Fred'))  # Try to convert a non-integer
        elif r == 2:
            [][2] = 5   # Try to assign to a nonexistent index of the empty list
        elif r == 3:
            print({}[1]) # Try to use a nonexistent key to get an item from a dictionary
        else:
            print(3 / 0)    # Try to devide by zero
    except ValueError:
        print('cannot convert integer')
    except IndexError:
        print('List index is out of range')
    except ZeroDivisionError:
        print('Division byzero not allowed')
    
    print('End of lop iteration', i)        