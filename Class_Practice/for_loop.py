str_a = "Hello"
for i in str_a:
    print(i)

lst_a = [1, 3, 5, 8]
for i in lst_a:
    print(i)

dict_a = {"a":1, "b":2}
for keys, values in dict_a.items():
    print(keys)
    print(values)

dict_b = {"vegetables":["Tomato", "Onion"], "fruits":["Apple", "Orange"]}
for k, v in dict_b.items():
    print(k)
    print(v)

tpl_a = (1, 4, 9)
for j in tpl_a:
    print(j)

set_a = {1, 6, 0}
initial = 0
for k in set_a:
    initial = k
    print(k)
print(initial)

# String reversing without using inbuilt function and without using slicing

str_b = "Deekshitha"
rev_str = ""
for i in str_b:
    print("The rev_str value before iteration is {}".format(rev_str))
    print("The value of i is {}".format(i))
    rev_str = i+rev_str
    print("the rev_str value after iteration is {}".format(rev_str))

print("The value of reversed string is {}".format(rev_str))

"""
i/p :  str_b = "Welcome to python"
o/p :  rev_str_b = "emocleW ot nothyp"

"""