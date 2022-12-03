count = 0
while count <= 6:
    print("loop continues")
    count = count + 1
print(count)

count = 0
while count <= 6:
    print(count)
    # print("loop continues")
    if count == 3:
        break
    count = count + 1
print(count)

count = 0
while count <= 6:
    count = count + 1

    if count == 3:
        continue
    print(count)
print(count)
