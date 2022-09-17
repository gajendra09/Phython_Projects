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