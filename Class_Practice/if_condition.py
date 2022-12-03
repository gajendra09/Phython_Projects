# to check even number

num = int(input("The number is : "))        # by default input function takes string
if num % 2 == 0:
    print("The given number is even")
else:
    print("The given number is not even")

# find the largest number among 3

a = int(input("Tha value a is : "))
b = int(input("The value of b is : "))
c = int(input("The value of c is: "))
if a > b and a > c:
    print("a is largest number")
elif b>a and b>c:
    print("b is largest number")
else:
    print("c is largest number")
if a>b:
    if a>c:
        print("a is largest ")

elif b>a:
    if b>c:
        print("b is largest")
else:
    print("c is largest")


lst = [3, 0, 5, 4]
len_lst = len(lst)
for i in range(len_lst):
    for j in range(i + 1, len_lst):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print("the ascending order of a list is {}".format(lst))

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print("the descending order of the list is {}".format(lst))

# find the list of even numbers and list of odd number from given list
lst_a = [2, 6, 9, 13, 22, 10, 33, 21, 4, 8]
lst_evn = []
lst_odd = []
for i in lst_a:
    if i % 2 == 0:
        lst_evn.append(i)
    else:
        lst_odd.append(i)

print("the list of even numbers is {}".format(lst_evn))
print("the list of odd numbers is {}".format(lst_odd))




