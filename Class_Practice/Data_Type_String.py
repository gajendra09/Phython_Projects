"""5 types  of data types
1. string
2. list
3. tuple
4. dictionary
5. set

it divides into 2 types
mutable:  the data can be changed after declaring a variable
1. list
2. dictionary
3. set
immutable: the data cannot be changed after declaring a variable
1. string
2. tuple
"""

"""
What is string?
string is sequence of elements which can be alphabet, numeric and alphanumeric, which is represented between double quotation
*** string is immutable
"""

x = "Python@3"

# finding type of a variable
type_x = type(x)
print("The type of variable x is {}".format(type_x))

# converting string to int
y = "8"     #type of 8 is string
type_y_bef_con = type(y)
print("The type of y variable before converting is {}".format(type_y_bef_con))
con_y = int(y)
type_y_aft_con = type(con_y)
print("The value of variable y after converting is {}".format(type_y_aft_con))

con_y_to_str = str(con_y)
type_con_y_to_str = type(con_y_to_str)
print("The type of variable y after converting back to str is {}".format(type_con_y_to_str))

# Indexing
str = "python"
len_str =len(str)
print("The length of str is {}".format(len_str))

zer_ind_str = str[0]
print("The value of zeroeth index of str is {}".format(zer_ind_str))
frst_ind_str = str[1]
print("The value of first index of str is {}".format(frst_ind_str))
scd_ind_str = str[2]
print("the value of second index is {}".format(scd_ind_str))
thrd_ind_str = str[3]
print("The value of third index of str is {}".format(thrd_ind_str))
frth_ind_str = str[4]
print("The value of fourth index is {}".format(frth_ind_str))
fft_ind_str = str[5]
print("The value of fifth index is {}".format(fft_ind_str))

# Reverse indexing

str = "python"

frst_neg_str = str[-1]
print("The value of first negative index of string is {}".format(frst_neg_str))

scnd_neg_str = str[-2]
print("The value of second negative index of string is {}".format(scnd_neg_str))

thrd_neg_str = str[-3]
print("The value of third negative index of string is {}".format(thrd_neg_str))

frth_neg_str = str[-4]
print("The value of fourth negative index of string is {}".format(frth_neg_str))

fif_neg_str = str[-5]
print("The value of fifth negative index of string is {}".format(fif_neg_str))

six_neg_str = str[-6]
print("The value of sixth negative index of string is {}".format(six_neg_str))

# Slicing

str_zer_to_sec_ind = str[0:3]
print("The value of slicing from zero to second index of a string is {}".format(str_zer_to_sec_ind))

str_two_to_fifth = str[2:6]
print("The value of slicing from second to fifth index of a string is {}".format(str_two_to_fifth))

str_four_to_five = str[4:6]
print("The value of slicing from fourth to fifth index of string is {}".format(str_four_to_five))

rev_one = str[-5:-1]
print("The value of reversing string is {}".format(rev_one))

rev_to_rev = str[1:-2]
print("The value of reverse to reverse string is {}".format(rev_to_rev))

rev_to_lst = str[-5::]
print("The value till last with reverse indexing is {}".format(rev_to_lst))

# string reversing
str_rev = str[::-1]
print("The value of reversed string is {}".format(str_rev))

print("The value of string with two colons is {}".format(str[::]))

# String capitalize
str_x = "welcome to python"
print("The value of string after capitalising is {}".format(str_x.capitalize()))

# count of a substring in a string
str_y = "Welcome to python and to class"
# print(len(str_y))
print("The count of string to in a given string is {}".format(str_y.count("to")))
print("The count of string o in a given string is {}".format(str_y.count("o")))

# find in string
print("The position of string to starting from is {}".format(str_x.find("to")))
print("The position of string to starting from is {}".format(str_y.find("to")))

# index in string
print("The position of string to starting from is {}".format(str_x.index("to")))
print("The position of string to starting from is {}".format(str_x.index("to", 7, 12)))
print("The position of string to starting from is {}".format(str_y.index("to", 7, 27)))

# startswith in string
print("The string startswith w is {}".format(str_x.startswith("w")))
print("The string startswith w is {}".format(str_x.startswith("p")))

# endswith inn string
print("The string endswith w is {}".format(str_x.endswith("w")))
print("The string endswith w is {}".format(str_x.endswith("n")))

# replace in string
str_sen = "Basket contains an apples, banana and oranges"
print("The value of string before replacement is {}".format(str_sen))
rep_str = str_sen.replace("banana", "grapes")
print("The value of string after replacing is {}".format(rep_str))

#  split  and join function
spl_str_spac = str_sen.split(" ")
print("The value after splitting spaces is {}".format(spl_str_spac))

join_spl_ele = ":".join(spl_str_spac)
print("the vallue of string after joining is {}".format(join_spl_ele))
jn_ele = "".join(spl_str_spac)
print("the value of string without space is {}".format(jn_ele))

# lower case in string
str_z = "Hello wORld"
lower_str = str_z.lower()
print("the value of string with lower case is {}".format(lower_str))

# upper case in string
upp_str = str_z.upper()
print("The value of string after converting to upper case is {}".format(upp_str))

# swapcase in string
swap_str = str_z.swapcase()
print("the value of string after swaping is {}".format(swap_str))

# check isalpha, isnumeric, isupper, islower, isalnum, isdecimal
str1 = "python"
str2 = "123"
str3 = "python36"
str4 = "WelcoMe"

is_alpha_str = str1.isalpha()
print("The given string is alpah: {}".format(is_alpha_str))
is_not_alpha = str1.isnumeric()
print("The given string is alpah: {}".format(is_not_alpha))

is_num_str = str2.isnumeric()
print("The given string is numeric: {}".format(is_num_str))

is_not_num = str2.isalpha()
print("The given string is numeric: {}".format(is_not_num))

is_alphnum = str3.isalnum()
print("The given string is alpha numeric: {}".format(is_alphnum))

is_lower = str4.islower()
print("The given string is lower: {}".format(is_lower))
is_upper = str4.isupper()
print("The given string is upper: {}".format(is_upper))

# string concatenation
str_a = "welcome"
str_b = "to"
str_c = "python"
str_space = " "
# o/p: "Welcome to python"
str_con1 = str_a+str_space+str_b+str_space+str_c
print("The value of string after concatenation is {}".format(str_con1))
str_con2 = str_a+" "+str_b+" "+str_c
print("The value of string after concatenation is {}".format(str_con2))

a = 2**10
print(a)
b = "welcome \nto \n\"python\""
print(b)
