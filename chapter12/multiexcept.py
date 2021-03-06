# Listing 12.6
# Offers three except blocks. Its try statement specifically can catch 
# ValueError, IndexError, and ZeroDivisionError exceptions.
# Author: Rick Halterman
# Last modified: 

import random

for i in range(10):     # Loop 10 times
    print('Beginning of loop iteration', i)
    try:
        r = random.randint(1, 3)    # r is pseudorandomly 1, 2, or 3
        if r == 1:
            print(int('Fred'))  # Try to convert a non-integer
        elif r == 2:
            [][2] = 5   # Try to assign to a nonexistent index of the empty list
        else:
            print(3 / 0)    # Try to devide by zero
    except ValueError:
        print('Connot convert integer')
    except IndexError:
        print('List index is out of range')
    except ZeroDivisionError:
        print('Division by zero not allowed')
    
    print('End of lop iteration', i)