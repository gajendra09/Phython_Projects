"""What is decorator?
Decorator allows us to wrap another function in order to extend
the behaviour of wrapped function without modifying behaviour of it.
any callable python object that is used to modify a function or a class
"""

def mult(func):
    def wrapper():
        x = func()
        return x*x
    return wrapper


@mult
def num():
    return 10
print(num())


def sum(func):
    def wrapper():
        a, b = func()
        return (a+b)*10
    return wrapper

@sum
def sm():
    return 8, 5
print(sm())


# decorate a function to give (a+b)*10

# monkey patching : it refers to modifying or updating a piece of code or class or any module at the run time
# *args: it is used to pass a variable number of arguments to a function
# **kwargs : it is used to pass keyworded, variable should length argument it may be list, tuple or dictionary

def arg_func(*args):
    for i in args:
        print(i)
arg_func("vandana","gajendra","prathibha")

def kwargs_func(**kwargs):
    print(kwargs)
kwargs_func(first = 6, second =5)