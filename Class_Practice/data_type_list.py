"""
what is list?
List is a group of elements which can be alphabets, numbers and alphanumeric or combinations of all which is represented between square braces.
*** List is mutable
"""

# declaring empty list
empty_lst = []
print("type 1 declaration of empty list is {}".format(empty_lst))

# another way of declaring empty list
emp_lst = list()
print("type 2 of declaringempty list is {}".format(emp_lst))


lst = [1, "a", "@", "10", "python@3"]
print("The value of list is {}".format(lst))
type_lst = type(lst)
print("The type of variable lst is {}".format(type_lst))

# Appending in list (only single element can be appended)
lst.append("Gajendra")
print("The value of list afetr appending is {}".format(lst))

# Extending in  list  (Only list of elements can be extended)
ext_lst = ["Vandana", "Abishek"]
lst.extend(ext_lst)
print("The value of list after extending is {}".format(lst))


lst_y = [1, "python"]
# print thon from list
ind_lst_y= lst_y[1]
# print(lst_y[1][2:6])
sec_to_fif_ind_lst_y = ind_lst_y[2:6]
print("The indexing of first element of list is {}".format(sec_to_fif_ind_lst_y))
print("The type of zeroeth index value of list is {}".format(type(lst_y[0])))
print("The type of first index value of list is {}".format(type(lst_y[1])))

# List concatination
lst1 = ["a", "b"]
list2 = [1, 2]
con_lst = lst1 + list2
print("The value of list after concatinating is {}".format(con_lst))

em_lst = []
em_lst.append("Deekshitha")
print("The value of empty list after appending is {}".format(em_lst))

# finding length of list

len_lst = len(con_lst)
print("The length of list is {}".format(len_lst))

# finding and max and minn number from list
lst_a = [4, 3, 8, 20, 1, 0]
max_num = max(lst_a)
min_num = min(lst_a)
print("The minimum number in list is {}".format(min_num))
print("The maximum number in list is {}".format(max_num))

# converting tuple to list
tple = ("a", "b", 1)
tple_to_lst = list(tple)
print("the value of converted tuple is {}".format(tple_to_lst))

# count the object occured in list

lst_b = [1, "a", "1", 2, 1]
count_int_1 = lst_b.count(1)
print("The count of element or object  of int 1 is {}".format(count_int_1))
count_str_1 = lst_b.count("1")
print("The count of element or object  of str 1 is {}".format(count_str_1))

# finding index of an object
ind_obj = lst_b.index("a")
print("The index value of object a is {}".format(ind_obj))

# inserting an object with the reference of index value
lst_b.insert(3, "c")
print("the value of list after inserting 3 to list is {}".format(lst_b))

# pop elmeent from list
lst_b.pop()
print("The value of list after popping an elemnt is {}".format(lst_b))
lst_b.pop(1)
print("the value of list after popping 1st index value is {}".format(lst_b))
# remove in list
lst_b.remove("1")
print("The value of list after removing string 1 is {}".format(lst_b))

# reverse in list
lst_b.reverse()
print("The value of list after reversing is {}".format(lst_b))

# sorting in list
lst_c = [5, 4, 9, 34, 65, 0, 23, 6]
lst_c.sort()
print("The value of list after sorting is {}".format(lst_c))

# zip in list
lsta = ["a", "b"]
lstb = [1, 2]
lst_zip =  list(zip(lsta, lstb))
print("The value after zipping 2 lists is {}".format(lst_zip))

sum_lstc = sum(lst_c)
print("The sum of list is {}".format(sum_lstc))