#Using list comprehension, create a list of squares for numbers from 1 to 10.

def list_of_squares(number):
     return [x**2 for x in range(1,number+1)]


print(list_of_squares(10))
