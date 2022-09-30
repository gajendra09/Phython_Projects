def str_rev(str):
    """
    str_rev : function name
    str : argument to the function
    """
    rev_str = ""
    for i in str:
        rev_str = i + rev_str
    return rev_str

str_a = str_rev("python")
print("The reversed value of str_a is {}".format(str_a))

str_b = str_rev("Hello world")
print("The reversed value of str_b is {}".format(str_b))


def rever_str(str):
    splt_str = str.split(" ")
    rev_lst = []
    for i in splt_str:
        rev_lst.append(i[::-1])
    splt_str = " ".join(rev_lst)
    return splt_str


str_c = rever_str("Welcome to python")
print("the reversed value of string is {}".format(str_c))

# write a method to sum of all elements in list
# write a method to find cubes of elements in list




