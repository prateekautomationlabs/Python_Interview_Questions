

def func(*args,**kwargs):
    print(args) # Tuple of positional args (1, 2, 'hello')
    print(kwargs)   # Dict of keyword args {'a': 3, 'b': 4}

func(1, 2,"hello", a=3, b=4) #no positional argument allowed after keyword argument