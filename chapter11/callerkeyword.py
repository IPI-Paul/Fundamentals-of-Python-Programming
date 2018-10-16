# Listing 11.15
# Shows how we can send a dictionary as a parameter to a function that expects 
# regular positional parameters
# Author: Rick Halterman
# Last modified: 

def f(a, b, c):
    print('a =', a, ' b =', b, ' c =', c)

f(1, 2, 3)          # Pass three parameters
dict = {}
dict['b'] = 22
dict['a'] = 11
dict['c'] = 33
f(**dict)
f(**{'a':10, 'b':20, 'c':30})   # Pass a dictionary