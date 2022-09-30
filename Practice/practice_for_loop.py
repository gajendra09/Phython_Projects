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







