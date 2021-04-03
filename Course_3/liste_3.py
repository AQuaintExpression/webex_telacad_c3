l = [5, 2, 1, 19, 4]

l2 = []
for element in l:
    l2.append(element ** 2)

for i in range(len(l)):
    l[i] = l[i] ** 2


print(l)
print(l2)

