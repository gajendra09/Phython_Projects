"""
what is tuple?
tuple is a group of elements which can be alphabets, numbers and alphanumeric or combinations of all which is represented between small braces.
*** tuple is immutable
"""

"""
Difference between list and tuple

List                                    Tuple
1. List is mutable                      1. Tuple is immutable
2. List can be appended and extended    2. Tuple cannot be appended or extended
3. List is slow                         3. Tuple is fast
4. List  allocates extra memory space   4. Tuple allocates memory space only for the declared elements
"""

"""
Why list is slow thann tuple?
during run time it checks for all the memory space allocated for list where list has extra memory space, hence list is slow and tuple doesnthave extra memory space allocate
hence tuple is fast.
"""

# One way of declaring empty tuple

empt_tup = ()
print("The vale of empty tuplpe is {}".format(empt_tup))
emp_tp = tuple()
print("The another way of creating empty tuple is {}".format(emp_tp))

tpl = (1, "a", "python@3")
print("The value of tuple is {}".format(tpl))

type_tpl = type(tpl)
print("the of tuplle is {}".format(type_tpl))

len_tpl = len(tpl)
print("The length of tuple is {}".format(len_tpl))

tple = (6, 2, 0, 2, 1)
min_num = min(tple)
max_num = max(tple)
print("The maximum value in tuple is {}".format(max_num))
print("The minimum value in tuple is {}".format(min_num))


