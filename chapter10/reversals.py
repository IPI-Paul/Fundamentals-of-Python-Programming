# Listing 10.23
# Exposes the major differences amongst the three reversal techniques of lists
# Author: Rick Halterman
# Last modified: 

lst = [1, 2, 3, 4, 5, 6, 7]
print('---- Original list ----')
print('lst =', lst)
print('---- reversed function ----')
obj1 = reversed(lst)
print('lst =', lst)
print('obj1 =', obj1)
print('---- Slice ----')
obj2 = lst[::-1]
print('lst =', lst)
print('obj2 =', obj2)
print('---- list.reverse method ----')
obj3 = lst.reverse()
print('lst =', lst)
print('obj3 =', obj3)