#Lambda functions are anonymous, single-expression functions in Python.
# They're super useful when you want quick, throwaway functionality without needing to formally define a function using def.
#Syntax lambda arguments: expression

add = lambda x,y : x+y
print(add(3,5))

mul = lambda x,y : x*y
print(mul(3,5))

numbers = [1,2,3,4]
sq_numbers = list(map(lambda x : x**2, numbers))
print(sq_numbers)

even_numbers = list(filter(lambda x : x%2==0, numbers))
print(even_numbers)