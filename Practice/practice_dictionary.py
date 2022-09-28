# dict_a = {"Name_1": "Abhishek", "Name_2", "Gajendra", "Name_3": "Vandana"}
#  reverse the values of given dict
# o/p:  dict_a = {"Name_1": "kehsihbA", "Name_2", "ardnejaG", "Name_3": "anadnaV"}

# add few more values to vegetables and fruits to existing dict3


list_a = ["Name_1", "Name_2", "Name_3"]
list_b = ["Abhishek", "Gajendra", "Vandana"]
dict_c = dict(zip(list_a, list_b))
print("The value of dictionary is {}".format(dict_c))
rev_list_b = list_b[0][::-1], list_b[1][::-1], list_b[2][::-1]
dict_b = dict(zip(list_a, rev_list_b))
print("the value of dictionary is {}".format(dict_b))

dict_a = {"Name_1": "Abhishek", "Name_2": "Gajendra", "Name_3": "Vandana"}
print("the value of dictionary is {}".format(dict_a))
val_dict = list(dict_a.values())[0][::-1], list(dict_a.values())[1][::-1], list(dict_a.values())[2][::-1]
print(" the values in dictionary are {}".format(val_dict))
get_keys = dict_a.keys()
print("the keys in the dictionary are {}".format(get_keys))

dict_c = dict(zip(get_keys, val_dict))
dict_a.update(dict_c)
print(" the value of dictionary is {}".format(dict_a))


lst1 = ["vegetables", "fruits"]
lst2 = [["beans", "carrot"], ["Apple", "Orange"]]
dict3 = dict(zip(lst1, lst2))
print("The value of dictionary from two lists is {}".format(dict3))

dict_a = {"Name_1": "Abhishek", "Name_2": "Gajendra", "Name_3": "Vandana"}
# dict_a["Name_1"] = dict_a["Name_1"][::-1]
# dict_a["Name_2"] = dict_a["Name_2"][::-1]
# dict_a["Name_3"] = dict_a["Name_3"][::-1]
# print(dict_a)



# frst_dict = dict_a["Name_1"]
# rev = frst_dict[::-1]
# print(frst_dict)
# print(rev)
# dict_a["Name_1"] = rev
# print(dict_a)

# print("the value of dictionary is {}".format(dict_a))
# val_dict = list(dict_a.values())[0][::-1], list(dict_a.values())[1][::-1], list(dict_a.values())[2][::-1]
# print(" the values in dictionary are {}".format(val_dict))
# get_keys = dict_a.keys()
# print("the keys in the dictionary are {}".format(get_keys))
# dict_c = dict(zip(get_keys, val_dict))
# dict_a.update(dict_c)
# print(" the value of dictionary is {}".format(dict_a))

# values = list(dict_a.values())
# lst_val = list((values[0][::-1], values[1][::-1], values[2][::-1]))
# print("The list  of reversed values are {}".format(lst_val))
# dict_a["Name_1"] = lst_val[0]
# dict_a["Name_2"] = lst_val[1]
# dict_a["Name_3"] = lst_val[2]
# print("The value of dict after reversing values are {}".format(dict_a))

# dict_a = {key: val[::-1] for key, val in dict_a.items()}
# print(dict_a)

dict3 = {"vegetables": ["beans", "carrot"], "fruits": ["apples", "orange"]}
# dict3["vegetables"] = dict3["vegetables"].append("Onion")
# dict3["fruits"] = dict3["fruits"].append("Grapes")
# print("the value of dict after updating is {}".format(dict3))

# fst = dict3["vegetables"]
# fst_lst = list(fst).append("a")
# print(fst_lst)
value = list(dict3.values())
val_app = [value[0]+["Onion"], value[1]+["Grapes"]]
dict3["vegetables"] = val_app[0]
dict3["fruits"] = val_app[1]
print(dict3)
