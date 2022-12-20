import regex as re

# Regex module is used for patterns, pattern matching or pattern searching

# search and span
txt = "welcome to oops concept"
s = re.search("oops", txt)
print(s.span())
# s = re.search("the", txt)
if s:
    print("pattern matched")
else:
    print("patter mismatch")

# findall method
txt1 = "malayalam"
x = re.findall("al", txt1)
print(x)

# sub
y = re.sub(" ", ",", txt)
print(y)


# pattern matching
txt2 = "python3"
z = re.findall("[0-9]", txt2)
# z = re.findall("[123]", txt2)
print(z)
a = re.findall("[yth]", txt2)
print(a)
b = re.findall("[a-zA-Z]", txt2)
print(b)
c = re.findall("[A-Z]", txt2)
print(c)
