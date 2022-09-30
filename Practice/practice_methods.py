def str_rev(str):
    rev_str = ""
    for i in str:
        rev_str = i+rev_str
    return rev_str


str_a = str_rev("Hello world")
print("the value of reversed string is {}".format(str_a))

str_b = str_rev("python")
print(str_b)