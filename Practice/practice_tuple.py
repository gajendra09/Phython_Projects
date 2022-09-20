"""
differnt ways of defining an empty tuple
1.empty_tuple = ()
2.emp_tpl = tuple()

decalre the tuple always between the small braces
"""
empty_tuple = ()
print("the value of tuple is {}".format(empty_tuple))
emp_tpl = tuple()
print("the value of tuple is {}".format(emp_tpl))

tpl = (1, "git", "pycharm", "#")
print("the value of tupple is {}".format(tpl))
len_tpl = len(tpl)
print("the length of tuple is {}".format(len_tpl))

zer_ind_tpl = tpl[0]
print("the value of zeroth index of tuple is {}".format(zer_ind_tpl))
frst_ind_tpl = tpl[1]
print("the value of first index of tupple is {}".format(frst_ind_tpl))
scnd_ind_tpl = tpl[2]
print("the value of second index of tuple is {}".format(scnd_ind_tpl))
thrd_ind_tpl = tpl[3]
print("the value of third index of tupple is {}".format(thrd_ind_tpl))

# negative indexing
frst_neg_tpl_ind = tpl[-1]
print("the value of first negative index of tuple is {}".format(frst_neg_tpl_ind))
scnd_neg_tpl_ind = tpl[-2]
print("the value of second negative index of tuple is {}".format(scnd_neg_tpl_ind))
thrd_neg_tpl_ind = tpl[-3]
print("the value of third negative index of tuple is {}".format(thrd_neg_tpl_ind))
frth_neg_tpl_ind = tpl[-4]
print("the value of fourth negative index of tuple is {}".format(frth_neg_tpl_ind))

# slicing of a tuple
slc_frst_to_third_tpl = tpl[1:4]
print("the slicing value from first to third index of tuple is {}".format(slc_frst_to_third_tpl))
slc_zero_to_second_tpl = tpl[0:3]
print("the slicing value from zeroth to second index of tuple is {}".format(slc_zero_to_second_tpl))
