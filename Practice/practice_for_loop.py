"""
i/p :  str_b = "Welcome to python"
o/p :  rev_str_b = "emocleW ot nothyp"

"""
# str_c = "Welcome to python"
# rev_str_c = ""
# for c in str_c:
#     print("the value of c is {}".format(c))
#     rev_str_c = c+rev_str_c
#     print("the value of reverse string is {}".format(rev_str_c))
#
# print("the value of reverse string is {}".format(rev_str_c))
# rev_str_b = rev_str_c[10:17]+rev_str_c[6:10]+rev_str_c[0:7]
# print("the value of reverse string is {}".format(rev_str_b))

str_b = "Welcome to python"
splt = str_b.split()
print(splt)
rev_str = ""
for i in splt:
    rev_str = i[::][::-1]+rev_str

print(rev_str)

# rev_splt = splt[0][::-1]+" "+splt[1][::-1]+" "+splt[2][::-1]
# print(rev_splt)

# rev_str = " "
# for r in str_b:
#     rev_splt = str_b.split()
#     print(rev_splt)
#     rev_str = rev_splt[0][::-1]+" "+rev_splt[1][::-1]+" "+rev_splt[2][::-1]
#     print(rev_str)





