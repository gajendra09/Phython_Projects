"""
str = "welcome to the world of python"
Print the value of string which is in the place of multiples of three

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
    print("the three multiple value are {}".format(str_x[i]))

lst_y = ["Malayalam", "area", "aba", "xyz", "see", "1221", "god"]
# count = 0
# for i in lst_y:
#     if i[0] == i[-1] and len(i) > 1:
#         print("palindrome elements in the list are {}".format(i))
#         count = 1 + count
# print("the count of palindrome elements in list are {}".format(count))
lsty_cm = [i for i in lst_y if i[0] == i[-1] and len(i) > 1]
print("the palindrome elements are {} and count is {}".format(lsty_cm, len(lsty_cm)))

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
    rev_nm = i + rev_nm
print("the value of reversed number is {}".format(rev_nm))
int_rv_nm = int(rev_nm)
diff_nm = nm - int_rv_nm
print("the difference between two numbers is {}".format(diff_nm))

lst_a = [4, 25, -2, 0, -9, 10, 3, -2, 4, 1]
lst_positive = []
lst_negative = []
for i in lst_a:
    if i >= 0 and i not in lst_positive:
        lst_positive.append(i)
    if i < 0 and i not in lst_negative:
        lst_negative.append(i)
print(lst_positive)
print(lst_negative)
lst_pos = [i for i in lst_a if i >= 0]
print(lst_pos)
str_a = "hgdkogfkkazmv591469sgh123agh"
str_dup = ""
for i in str_a:
    if i not in str_dup:
        str_dup = i + str_dup
print(str_dup)

lst_b = [5, 56, 17, 87, 34, 2, 76]
lst_b.sort()
lst_b.reverse()
print(lst_b)
N = int(input("N ="))
lar_lst = []
for i in range(N):
    lar_lst.append(lst_b[i])
print(lar_lst)


def large_number(list, N):
    large_lst = []
    list.sort()
    list.reverse()
    for i in range(N):
        large_lst.append(list[i])
    return large_lst


lst_c = large_number([54, 4, 76, 89, 9], 3)
print("the largest number in the list is {}".format(lst_c))

str3 = "abcdfcdaecbajadej"
str_dict = {}
for i in str3:
    cnt = str3.count(i)
    str_dict[i] = cnt
print(str_dict)

dict_str = {i: str3.count(i) for i in str3}
print(dict_str)

str_a = " hai how are you"
lst_x = ["a", "e", "i", "o", "u"]
str_dic = {}
for i in str_a:
    if i in lst_x:
        cont = str_a.count(i)
        str_dic[i] = cont
print(str_dic)
vovels_cm = {i: str_a.count(i) for i in str_a if i in lst_x}
print(vovels_cm)

str_b = " hai how are you"
lst = ["a", "e", "i", "o", "u"]
for i in str_b:
    if i in lst:
        str_b = str_b.replace(i, "")
print(str_b)

n = 17
for i in range(2, n):
    if n % i == 0:
        print("n is not a prime")
        break
else:
    print("n is a prime number")

str_c = "this is India"
spl_str_c = str_c.split()
lnth = 0
for i in spl_str_c:
    if len(i) > lnth:
        lnth = len(i)
print("the max length string is {}".format(i))
print("length is {}".format(len(i)))

str_w = "Welcome to python"
spl_str_w = str_w.split()
max_lent = max(spl_str_w, key=len)
print("the max length string is {} and length is {}".format(max_lent, len(max_lent)))

dict_a = {"a": 1, "b": 2, "c": 3}
dict_b = {"e": 5, "c": 4, "d": 5}

s = "abcabcbb"
s_s = ""
for i in s:
    if i not in s_s:
        s_s = s_s + i
print("the answer is {} and length is {}".format(s_s, len(s_s)))

t = "pythonnoh"
t_t = ""
for i in t:
    if i not in t_t:
        t_t = t_t + i
print("the answer is {} and length is {}".format(t_t, len(t_t)))

# to check given number is prime number or not
n = int(input("Enter the value :  "))
# n = 17
for i in range(2, n):
    if n % i == 0:
        print("n is not a prime")
        break
else:
    print(("n is a prime number"))

# To list prime numbers from range 1 to 50
prime_num = []
for j in range(1, 51):
    for i in range(2, j):
        if j % i == 0:
            break
    else:
        prime_num.append(j)
print(prime_num)

# str  = "this is India"
str1 = "welcome to python"
lst = str1.split(" ")
mx_ln = 0
mx_str = ""
for i in lst:
    if len(i) > mx_ln:
        mx_ln = len(i)
        mx_str = i
print("String {} has max length {}".format(mx_str, mx_ln))

s = "aaabbccddef"
index = 0
str_rep = ""
while (index <= len(s) - 1):
    count = 1
    char = s[index]
    j = index
    while (j < len(s) - 1):
        if (s[j] == s[j + 1]):
            count = count + 1
            j = j + 1
        else:
            break
    str_rep = str_rep + str(count) + char
    index = j + 1
print(str_rep)

dict_a = {"a": 1, "b": 2, "c": 3}
dict_b = {"e": 5, "c": 4, "d": 5}
for k in dict_b:
    if k in dict_a:
        dict_b[k] = dict_b[k] + dict_a[k]
res = dict_a | dict_b
print(res)

b = [{"name": "Tom", "age": "10"}, {"name": "Mark", "age": "5"}, {"name": "Pam", "age": "7"},
     {"name": "Sam", "age": "12"}]
dictb = {}
for i in b:
    v = i["name"]
    dictb[v] = int(i["age"])
print(dictb)
lstb = list(dictb.items())
lstb.sort()
dictbb = dict(lstb)
print(dictbb)

c = "welcome to python"
d = {"a", "e", "i", "o", "u"}
vovels_cd = {i: c.count(i) for i in c if i in d}
print(vovels_cd)

a = "i sabyasachi , techno exponent , sabyasachi exponent"
replc = a.replace(",", " ")
splta = replc.split()
dicta = {}
for i in splta:
    couunt = splta.count(i)
    dicta[i] = couunt
print(dicta)

x = list(range(0, 50, 7))
print(x)
