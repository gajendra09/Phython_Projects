"""
Set : set is a collection of elements which should be enclosed between curly braces.
      set is immutable, unordered and unindexed.
      set doesn't contain duplicate values.
"""
set_a = {1, "a", "g", 3, "a"}
print("the value of the set is {}".format(set_a))

lst = ["apple", "banana", "orange", "papaya"]
lst_to_set = set(lst)
print("the value of set after converting is {}".format(lst_to_set))

# to find the length of the set
len_set_a = len(set_a)
print("the length of set a is {}".format(len_set_a))

# to find the type of the set
type_lst_to_set = type(lst_to_set)
print("the type of the set is {}".format(type_lst_to_set))

# add elements to the set
lst_to_set.add("grapes")
print("the value of set after adding value is {}".format(lst_to_set))
upd_set = {"mango", "pineapple"}
lst_to_set.update(upd_set)
print("the value of set after updating elements is {}".format(lst_to_set))

# removing elements from set
rem_set = lst_to_set.remove("pineapple")
print("the value of the set after removing is {}".format(lst_to_set))

# discarding an element from set
dis_set =lst_to_set.discard("orange")
print("the value of the set after discording is {}".format(lst_to_set))

# popping of a set
pop_set = lst_to_set.pop()
print("the value of set after popping is {}".format(lst_to_set))

# to clear the set
clr_set = lst_to_set.clear()
print("the value of set after clearing is {}".format(lst_to_set))