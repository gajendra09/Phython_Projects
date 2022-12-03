x = lambda x: x * 5
print(x(5))

y = lambda x, y, z: (x + y) * z
print(y(10,20,5))

def add_5():
    return lambda a:a+8
a = add_5()
print(a(7))
