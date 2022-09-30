"""
What is set?
Set is a group of elements enclosed between {}, where set is immutable, unordered and unindexed.
Set doesn't contains duplicates
"""
set1 = {"a", "b", "c", "a"}
print("The value of set is {}".format(set1))

lst = [1, 2, 3, 1, 4, 5, 2]
lst_to_set = set(lst)
print("Te value of list to set is {}".format(lst_to_set))

len_set = len(lst_to_set)
print("The length of set is {}".format(len_set))

type_set = type(lst_to_set)
print("The type is {}".format(type_set ))

# add and update in set
set1.add("d")
print("The value of set after adding d is {}".format(set1))
upd_set = {"e", "f"}
set1.update(upd_set)
print("The value of set after updating is {}".format(set1))

#remove, discard and pop and clear in sets
"""
** Remove will raise error if element doesnot exist
** discard will not raise error if element doesnot exist
** pop will delete last element from set, but set is unordered and cannot know which element is getting removed
"""

rem_set1 = set1.remove("a")
print("The value after removing a is {}".format(set1))
dis_set1 = set1.discard("c")
print("The value after discard c is {}".format(set1))
pop_set1 = set1.pop()
print("The value after pop  is {}".format(set1))

clear_set = set1.clear()
print("The set after clearing is {}".format(set1))



# union and intersection
set_a = {"a", "b", 1, 2}
set_b = {"c", "a", "d"}
union_set = set_a.union(set_b)
print("The  union value of set_a and set_b is {}".format(union_set))
inter_seta_setb = set_a.intersection(set_b)
print("The intersection of set_a and set_b is {}".format(inter_seta_setb))
# inter_setb_seta = set_b.intersection(set_a)
# print("The intersection of  set_b and set_a is {}".format(inter_setb_seta))
