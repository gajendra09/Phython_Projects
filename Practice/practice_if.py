"""
str = "welcome to the world of python"
Print the value of string which is in the place of multiples of string

2. Remove duplicates from the list(lst= [1,4,1,5,2,4]

3.lst = ["malayalam", "area","dog"]
Print the elements of list which is starting and ending with same letter

num = 48
diff = 48-84


lst = ["Malayalam", "area", "aba", "xyz", "see", "1221", "god"]
op: 4
"""

lst = [1, 4, 1, 5, 2, 4]
lst_without_duplicate = []
for i in lst:
    if i not in lst_without_duplicate:
        lst_without_duplicate.append(i)

print(lst_without_duplicate)

"""
Remove duplicates from list

lst = [1, 4, 1, 5, 2, 4]
lst_dup = []
for i in lst:
    if i not in lst_without_duplicate:
        lst_without_duplicate.append(i)

print(lst_without_duplicate)

lst_dup = []

# 1st iteration:
i = 1
1 not in lst_dup:
lst_dup = [1]

# 2nd iteration:
i = 4
4 not in lst_dup:
lst_dup = [1, 4]


# 3rd iteration:
i = 1
1 not in lst_dup:
break
lst_dup = [1,4]

# 4th iteration:
i = 5
5 not in lst_dup:
lst_dup = [1, 4, 5]

# 5th iteration:
i = 2
2 not in lst_dup:
lst_dup = [1, 4, 5, 2]

# 6th iteration:
i = 4
4 not in lst_dup:
break
lst_dup= [1, 4, 5, 2]
"""
str_x = "welcome to the world of python"
for i in range(0, 30, 3):
    print(str_x[i])

lst_y = ["Malayalam", "area", "aba", "xyz", "see", "1221", "god"]
count = 0
for i in lst_y:
    if i[0] == i[-1] and len(i) > 1:
        print("palindrome elements in the list are {}".format(i))
        count = count + 1
print("the count of of palindrome elements in list are {}".format(count))


num = 48
str_num = str(num)
print(str_num)
rev_num = str_num[::-1]
print("the value of reversed number is {}".format(rev_num))
int_rev_num = int(rev_num)
diff = num - int_rev_num
print("the difference between two numbers is {}".format(diff))


nm = 56
str_nm = str(nm)
rev_nm = ""
for i in str_nm:
    rev_nm = i+rev_nm
print("the value of reversed number is {}".format(rev_nm))
int_rv_nm = int(rev_nm)
diff_nm = nm - int_rv_nm
print("the difference between two numbers is {}".format(diff_nm))


lst_a = [4, 25, -2, 0, -9, 10, 3, -2, 4, 1]
lst_positive = []
lst_negative = []
for i in lst_a:
    if i > 0 and i not in lst_positive:
        lst_positive.append(i)
    if i < 0 and i not in lst_negative:
        lst_negative.append(i)
print(lst_positive)
print(lst_negative)

str_a = "hgdkogfkkazmv591469sgh123agh"
str_dup = ""
for i in str_a:
    if i not in str_dup:
        str_dup = i + str_dup
print(str_dup)





























