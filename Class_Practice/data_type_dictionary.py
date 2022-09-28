"""
What is dictionary?
Dictionaries are set of key value pair or known as one to one mapping and
it enclosed between curley braces. Dictionary is itself mutable and keys inside the dictionaries are immutable
"""
emp_dict1 = dict()
print("The one way of declaring empty dictionary is {}".format(emp_dict1))
emp_dict2 = {}
print("The another way of empty dictionary is {}".format(emp_dict2))

dict1 = dict()
dict1["Name"] = "John"
print("The value of dictionary is {}".format(dict1))
dict1["Age"] = 23
dict1["salary"] = 100000
print("The value of dictionary after updating is {}".format(dict1))
dict2 = {"a": 1, "b": 1}
print("the value of dictionary is {}".format(dict2))

len_dict1 = len(dict1)
print("The length of dictionary is {}".format(len_dict1))

type_dict2 = type(dict2)
print("the type of dictionary is {}".format(type_dict2))
dict2.update({"c": 3, "d": 4})
print("The value of dictionary after updating is {}".format(dict2))

get_elem1 = dict1["Age"]                         # If suppose wer are trying to print value of a key which is not in dictionary,at this point it throws error
print("the value of age is {}".format(get_elem1))

# get_elem2 = dict1["a"]
# print("the value of a in dict1 is {}".format(get_elem2))

get_ele2 = dict2.get("a")                   # If suppose wer are trying to print value of a key which is not in dictionary,at this point it doenot throws error, but it returns None
print("The value of a ia {}".format(get_ele2))

get_ele3 = dict2.get("Age")
print("The value of age in dict2 is {}".format(get_ele3))

# Fetch keys and values from dictionary
get_keys = dict1.keys()
print("The value of keys are {}".format(get_keys))
print("The value of keys are {}".format(list(get_keys)))
get_values = list(dict1.values())
print("The dictionary value are {}".format(get_values))

get_items = dict2.items()
print("the items of dictionary are {}".format(get_items))

# pop and popitem in dictionary
pop_key_value = dict2.pop("a")
print("the value of dictioanry after popping a is {}".format(dict2))

pop_item = dict2.popitem()
print("the value of dictionary after popping an item is {}".format(dict2))

clear_dict = dict2.clear()
print("the value of dictionary after clearing is {}".format(clear_dict))

# how to create dictionary from two lists
lst1 = ["vegetables", "fruits"]
lst2 = [["beans", "carrot"], ["Apple", "Orange"]]
dict3 = dict(zip(lst1, lst2))               # list can be a values for dictionary but not keys, because keys are immutable and lists are mutable hence list cannot be a key for dictionary
print("The value of dictionary from two lists is {}".format(dict3))
