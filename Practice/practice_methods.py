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
    return cub_ls

list_x = cube_list([2, 3, 4, 5])
print("the cube values are {}".format(list_x))

list_y = cube_list([6, 7, 8, 9, 10])
print("the cube values are {}".format(list_y))

def dec_lst(list):
    list.sort()
    dec_list = []
    for i in list:
        dec_list = [i]+dec_list
    return dec_list

list_a = dec_lst([1, 77, 965, 4, 0])
print("the descending order value of list is {}".format(list_a))

list_b = dec_lst([8, 65, 98, 67, 99])
print("the descending order value of list is {}".format(list_b))

list_c = dec_lst([66, 44, 88, 898, 233])
print("the descending order value of list is {}".format(list_c))

def dict_datatype(dict):
    val_typ = []
    key_typ = []
    for key, val in dict.items():
        val_typ.append(type(val))
        key_typ.append(type(key))
    return val_typ, key_typ

dict_a = dict_datatype({"a": 1, "b": "2"})
print("the type of the dictionary is {}".format(dict_a))

dict_b = dict_datatype({"c": 5, "d": "apple", "e": [10, "33"], "f": (1, "python")})
print("the type of the dictionary is {}".format(dict_b))

def list_withou_duplicate(list):
    lst_without_duplicate = []
    for i in list:
        if i not in lst_without_duplicate:
            lst_without_duplicate.append(i)
    return lst_without_duplicate
lst = list_withou_duplicate([1, 4, 99, 4, 3, 1, 85, 3])
print("the list without duplicate is {}".format(lst))

def multiple_of_three(str):
    str_v = ""
    for i in range(3, 30, 3):
        str_v = str_v + str[i]
    return str_v
str_c = multiple_of_three("welcome to the world of python")
print("the three multiple values of string are {}".format(str_c))

def palindrome_count(list):
    count = 0
    for i in list:
        if i[0] == i[-1] and len(i) > 1:
            print("palindrome elements in the list are {}".format(i))
            count = count + 1
    return count

lst_a = palindrome_count(["malayalam", "area", "aba", "xyz", "see", "1221", "god"])
print("the count of palindromes in list are {}".format(lst_a))

def difference_reverse_number(num):
    str_nm = str(num)
    rev_nm = ""
    for i in str_nm:
        rev_nm = i + rev_nm
        int_rv_nm = int(rev_nm)
        diff_nm = num - int_rv_nm
    return diff_nm
int_a = difference_reverse_number(28)
print("the difference between number and reversed number is {}".format(int_a))

def pos_neg_remove_duplicates(list):
    lst_a = [4, 25, -2, 0, -9, 10, 3, -2, 4, 1]
    lst_positive = []
    lst_negative = []
    for i in lst_a:
        if i > 0 and i not in lst_positive:
            lst_positive.append(i)
        if i < 0 and i not in lst_negative:
            lst_negative.append(i)
    return lst_positive, lst_negative

lst_b = pos_neg_remove_duplicates([4, 25, -2, 0, -9, 10, 3, -2, 4, 1])
print(lst_b)

def remove_str_dup(str):
    str_dup = ""
    for i in str:
        if i not in str_dup:
            str_dup = i + str_dup
    return str_dup
str_d = remove_str_dup("hhfbbhjdksdghsdnhbhsdhgjhdeyeyen")
print("the value of string after removing duplicates is {}".format(str_d))


def decending_order_list(list):
    list.sort()
    list.reverse()
    N = int(input("N ="))
    lar_lst = []
    for i in range(N):
        lar_lst.append(list[i])
    return lar_lst
lst_c = decending_order_list([5, 56, 17, 87, 34, 2, 76])
print("the value of list for first three large numbers are {}".format(lst_c))


def vowels_string(str):
    lst_x = ["a", "e", "i", "o", "u"]
    str_dic = {}
    for i in str:
        if i in lst_x:
            cont = str.count(i)
            str_dic[i] = cont
    return str_dic
str_x = vowels_string("hai how are you")
print(str_x)

def remove_vowels(str):
    lst = ["a", "e", "i", "o", "u"]
    for i in str:
        if i in lst:
            str = str.replace(i, "")
    return str
str_y = remove_vowels("hai how are you")
print(str_y)

def prime_number(int):
    for i in range(2, int):
        if int % i == 0:
            print("n is not a prime")
            break
    else:
        print(("n is a prime number"))


num = prime_number(31)
print(num)
