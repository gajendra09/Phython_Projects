"""What is decorator?
Decorator allows us to wrap another function in order to extend
the behaviour of wrapped function without modifying behaviour of it
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
