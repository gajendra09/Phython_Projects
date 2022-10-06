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

