"""
i/p :  str_b = "Welcome to python"
o/p :  rev_str_b = "emocleW ot nothyp"
"""
str_a = "Welcome to python"
splt_str = str_a.split(" ")
rev_lst = []
for i in splt_str:
    rev_lst.append(i[::-1])

rev_lst = " ".join(rev_lst)

print(rev_lst)

list_a = [2, 3, 4, 8]
sum_list_a = 0
for i in list_a:
    sum_list_a = i+sum_list_a
print(sum_list_a)


cub_lst = []
for i in list_a:
    cub_lst.append(i*i*i)
print(cub_lst)


lst_a = [2, 4, 6, 9]
lst_b = [3, 4, 5, 2, 4]


lst = [3, 5, 1, 99, 2, 0]
lst.sort()
print("List after sorting  {}".format(lst))
desc_lst = []
for i in lst:
    desc_lst.insert(0, i)
    # desc_lst = [i]+desc_lst
print("descending order of list is {}".format(desc_lst))

dicta = {"a": 1, "b": "2"}
val_typ = []
for key, val in dicta.items():
    val_typ.append(type(val))
print("The type of values in dictionary is {}".format(val_typ))

# range function

lst = list(range(10))
print("the range value of list is {}".format(lst))

lst_x = list(range(20, 45))
print("the range value of list is {}".format(lst_x))

"""
step size : it tells us how many steps we skip from original sequence
   syntax : range(start, end, step)
"""

lst_y = list(range(0, 100, 5))
print("the range value of step list is {}".format(lst_y))


lst = [" ABC ", "hcb", " xyz"]
Outp: lst =["ABC","hcb","xyz"]

lst = [" ABC ", " hcb", "xyz"]
for i in range(len(lst)):
    if " " in lst[i]:
        str = lst[i].replace(" ", "")
        lst[i] = str
print(lst)
