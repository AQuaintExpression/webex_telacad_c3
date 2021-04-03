#    b. printeaza suma multiplilor de 3 sau 5 in intervalul [1, n].
#    eg: 3, 5, 6, 9, 12, 15 pentru n = 17

n = int(input('n = '))

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)


