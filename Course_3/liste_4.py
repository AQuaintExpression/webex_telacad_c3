l = [6, 2, 19, 14, 13, 10]

# vrem sa obtinem patratele numerelor pare

rez = []
for nr in l:
    if nr % 2 == 0:
        rez.append(nr ** 2)

print(rez)
