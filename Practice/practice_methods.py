def str_rev(str):
    rev_str = ""
    for i in str:
        rev_str = i+rev_str
    return rev_str


str_a = str_rev("Hello world")
print("the value of reversed string is {}".format(str_a))

str_b = str_rev("python")
print(str_b)

def sum_list(list):
    sum_lst = 0
    for i in list:
        sum_lst = i+sum_lst
    return sum_lst


list_c = sum_list([4, 8, 27, 37])
print("the sum of the list is {}".format(list_c))

list_d = sum_list([7, 18, 29, 31])
print("the sum of the list is {}".format(list_d))

def cube_list(list):
    cub_lst = []
    for i in list:
        cub_lst.append(i*i*i)
    return cub_lst

list_x = cube_list([2, 3, 4, 5])
print("the cube values are {}".format(list_x))

list_y = cube_list([6, 7, 8, 9, 10])
print("the cube values are {}".format(list_y))
