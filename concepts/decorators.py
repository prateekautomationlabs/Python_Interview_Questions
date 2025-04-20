#Decorators are functions that modify the behavior of other functions or methods.
# They are often used for logging, access control, or instrumentation.
#Most important defination: A decorator is a function that takes another function and
# adds functionality to it without modifying its structure.

def decorator_func(func):
    def wrapper():
        print(f"\n🔍 Running function: {func.__name__}")
        func()
        print(f"\n🔍 Execution Completed: {func.__name__}")
    return wrapper

@decorator_func
def say_hello():
    print("Hello")

say_hello()