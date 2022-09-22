"""
we have two ways to print an empty list
1. empty_lst = []
2. emp_lst = lst()
"""

lst = [2, "hello", "g", "python", "@", "9"]
print("the value of list is {}".format(lst))
type_lst = type(lst)
print("the type of list is {}".format(type_lst))

# appending a value to the existing list
lst.append("abc")
print("the value of list after appending a value is {}".format(lst))

# extending list by adding value
ext_lst = ["pqr", "xyz", "123"]
lst.extend(ext_lst)
print("the value of list after extending is {}".format(lst))

len_lst = len(lst)
print("the length of list is {}".format(len_lst))

zer_ind_lst = lst[0]
print("the value of zeroth index of list is {}".format(zer_ind_lst))
frst_ind_lst = lst[1]
print("the value of first index of list is {}".format(frst_ind_lst))
scnd_ind_lst = lst[2]
print("the value of second index of list is {}".format(scnd_ind_lst))
thrd_ind_lst = lst[3]
print("the value of third index of list is {}".format(thrd_ind_lst))
frth_ind_lst = lst[4]
print("the value of fourth index of list is {}".format(frth_ind_lst))
ffth_ind_lst = lst[5]
print("the value of fifth index of list is {}".format(ffth_ind_lst))
sxth_ind_lst = lst[6]
print("the value of sixth index of list is {}".format(sxth_ind_lst))
snth_ind_lst = lst[7]
print("the value of seventh index of list is {}".format(snth_ind_lst))
egth_ind_lst = lst[8]
print("the value of eighth index of list is {}".format(egth_ind_lst))
ninth_ind_lst = lst[9]
print("the value of ninth index of list is {}".format(ninth_ind_lst))

# negative indexing
neg_frst_lst_ind = lst[-1]
print("the value of first negative index of list is {}".format(neg_frst_lst_ind))
neg_scnd_lst_ind = lst[-2]
print("the value of second negative index of list is {}".format(neg_scnd_lst_ind))
neg_thrd_lst_ind = lst[-3]
print("the value of third negative index of list is {}".format(neg_thrd_lst_ind))
neg_frth_lst_ind = lst[-4]
print("the value of fourth negative index of list is {}".format(neg_frth_lst_ind))
neg_ffth_lst_ind = lst[-5]
print("the value of fifth negative index of list is {}".format(neg_ffth_lst_ind))
neg_sxth_lst_ind = lst[-6]
print("the value of sixth negative index of list is {}".format(neg_sxth_lst_ind))
neg_snth_lst_ind = lst[-7]
print("the value of seventh negative index of list is {}".format(neg_snth_lst_ind))
neg_egth_lst_ind = lst[-8]
print("the value of eighth negative index of list is {}".format(neg_egth_lst_ind))
neg_nnth_lst_ind = lst[-9]
print("the value of ninth negative index of list is {}".format(neg_nnth_lst_ind))
neg_tnth_lst_ind = lst[-10]
print("the value of tenth negative index of list is {}".format(neg_tnth_lst_ind))

# slicing of list
slc_zer_to_fifth_ind = lst[0:6]
print("the slicing value from zeroth to fifth index is {}".format(slc_zer_to_fifth_ind))
slc_scnd_to_ninth_ind = lst[2:10]
print("the slicing value from second to ninth index is {}".format(slc_scnd_to_ninth_ind))
slc_frst_to_sxth_ind = lst[1:7]
print("the slicing value from first to sixth index is {}".format(slc_frst_to_sxth_ind))
slc_neg_ind_ = lst[-10:-1]
print("the value is {}".format(slc_neg_ind_))


lst_x = ["Vandana", "Abhishek", "Gajendra", "Manasa"]
rev_lst_x = lst_x[0][::-1], lst_x[1][::-1], lst_x[2][::-1], lst_x[3][::-1]
print("the value of reversed list is {}".format(rev_lst_x))

frst_rev_lst_x = lst_x[0][::-1]
scnd_rev_lst_x = lst_x[1][::-1]
thrd_rev_lst_x = lst_x[2][::-1]
frth_rev_lst_x = lst_x[3][::-1]
print("the value of reversed list x is {}, {}, {}, {}".format(frst_rev_lst_x, scnd_rev_lst_x, thrd_rev_lst_x, frth_rev_lst_x))



