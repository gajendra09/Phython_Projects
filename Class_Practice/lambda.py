# lambda: a Lambda function can take any number of arguments but it can have only one expression

x = lambda a: a + 5
print(x(10))


def add_5():
    return lambda a: a + 5


b = add_5()
print(b(5))

y = lambda a, b: a * b
print(y(3, 4))


def mult():
    return lambda a, b: a * b


a = mult()
print(a(3, 4))


def func(n):
    return lambda a: a * n


z = func(6)
print(z(4))


def add(n):
    return n + n


num = (2, 7, 8, 9)
res = map(add, num)
print(list(res))

numbers = (5, 7, 8)
res = map(lambda x: x + x, numbers)
print(list(res))

num_a = [2, 9, 8, 7]
num_b = [5, 1, 3, 6]
research = map(lambda x, y: x + y, num_a, num_b)
print(list(research))

num = [5, 7, 8, 2, 4, 10, 1, 3, 22, 6]
fil_eve = filter(lambda a: a % 2 == 0, num)
fil_odd = filter(lambda a: a % 2 != 0, num)
print("filtered even numbers are:{}".format(fil_eve))
print("filtered odd numbers are:{}".format(fil_odd))

z = lambda x: True if x < 10 else False
print(z(2))
print(z(11))

num = {5, 7, 8, 2, 4, 10, 1, 3, 22, 6}
fil_eve = filter(lambda a: a % 2 == 0, num)
fil_odd = filter(lambda a: a % 2 != 0, num)
print("filtered even numbers are:{}".format(list(fil_eve)))
print("filtered odd numbers are:{}".format(set(fil_odd)))

dict_a = {"a": "1", "b": "2"}
fil = filter(lambda a: a, dict_a.items())
print(list(fil))

z = lambda x: True if x < 10 else False
print(z(2))
print(z(11))

str = "python"
rev_str = ""
count = 0
len_str = len(str)
while count < len_str:
    rev_str = str[count] + rev_str
    count += 1
print(rev_str)

# List comprehension
lst_a = [2, 4, 5, 8]
lst_b = [4, 6, 9, 10]
lst = [lst_a[i] + lst_b[i] if len(lst_a) == len(lst_b) else None for i in range(len(lst_b))]
print(lst)

num = [20, 10, 9]
lst_1 = [i if i > 10 else i + 1 for i in num]
print(lst_1)

# dictionary comprehension
dict = {lst_a[i]: lst_b[i] for i in range(len(lst_b)) if len(lst_a) == len(lst_b)}
print(dict)
# during if else condition for should be at end and during only if for should be before if condition

lst_2 = [2, 9, 1, 3, 6, 5]
lst_cm = [i * i for i in lst_2]
print(lst_cm)
dict_1 = {i: i * i for i in lst_2}
print(dict_1)

# deep copy and shallow copy generators reduce
# python packaging

lst1 = [1, 2, 3, 4, 9]
lst2 = [5, 6, 7, 8]
try:
    sum_lst = []
    for i in range(len(lst1)):
        sum2 = lst1[i] + lst2[i]
        sum_lst.append(sum2)
    print("The sum of each elements of two two list is {}".format(sum_lst))
except Exception as e:
    print(e)

n = int(input("Enter the value : "))
try:
    if n % 2 == 0:
        print("The given value is even")
    else:
        print("The given value is odd")
except:
    print("Exception occurred")
else:
    print("went good without any exception")



