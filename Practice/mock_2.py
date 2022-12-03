str = "abcdfcdaecbajadej"
lst = ["a", "e", "i", "o", "u"]
str_dict = {}
for i in str:
    if i in lst:
        cnt = lst.count(i)
        str_dict[i] = cnt
print(str_dict)

str_dup = ""
for i in str:
    if i not in str_dup:
        str_dup = i + str_dup
print(str_dup)


def lar_num(list, N):
    list.sort()
    list.reverse()
    lar_lst = []
    for i in range(N):
        lar_lst.append(list[i])
    return lar_lst

lst_a = ["malayalam", "area", "dog"]
pal_lst = []
for i in lst_a:
    if i[0] == i[-1]:
        pal_lst.append(i)
print(pal_lst)

lst_b = ["a", "b"]
dict = {"e": 2, "f": 6, "k": 9, "b": 1}
# for i, k in dict.items():
for i in lst_b:
    if i in list(dict.keys()):
        dict.pop(i)
print(dict)

str_a = "hello world"
splt_str = str_a.split()
rev_lst = []
for i in splt_str:
    rev_lst.append(i[::-1])
rev_str = " ".join(rev_lst)
print(rev_str)

