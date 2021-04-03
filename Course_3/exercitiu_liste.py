
#eliminati toate valorile de 2 din l

# l.pop(poz)
# l.remove(valoare)


# while 2 in l:
#     l.remove(2)
#
# print(l)
l = [1, 2, 9, 2, 2, 6, 2, 3]
cnt = 0
for n in l:
    if n == 2:
        cnt += 1

for i in range(cnt):
    l.remove(2)

print(l)