
# == checks if two variables have the same value.
# is checks if two variables point to the same object in memory

a = [1,2,3]
b = a
c = [1,2,3]

print(a is b) # True: same object
print( a is c) # False: different objects
print(a == b) #True
print(a == c) # True: values are equal