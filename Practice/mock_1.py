# write a method to get a decending order of a list using foeloop

def dec_lst(list):
    list.sort()
    dec_list = []
    for i in list:
        dec_list = [i] + dec_list

    return dec_list


list_a = dec_lst([1, 77, 965, 4, 0])
print("the descending order value of list is {}".format(list_a))

list_b = dec_lst([8, 65, 98, 67, 99])
print("the descending order value of list is {}".format(list_b))

list_c = dec_lst([66, 44, 88, 898, 233])
print("the descending order value of list is {}".format(list_c))


def dict_datatype(dict):
    val_typ = []
    for key, val in dict.items():
        val_typ.append(type(val))
    return val_typ


dict_a = dict_datatype({"a": 1, "b": "2"})
print("the type of the dictionary is {}".format(dict_a))

dict_b = dict_datatype({"c": 5, "d": "apple", "e": [10, "33"], "f": (1, "python")})
print("the type of the dictionary is {}".format(dict_b))

mystring = "i sabyasachi , techno exponent , sabyasachi exponent"
replc = mystring.replace(",", "")
print(replc)
