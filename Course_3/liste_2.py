l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9  #index +
 # -10,-9,-8,-7,-6,-5,-4,-3,-2,-1  #index -

#exemple slicing cu liste
# print(l[0:6])
# print(l[:-4])
#
# print(l[::-1])
# print(l[0::2]) #numerele pare
# print(l[1:9:2])

# concatenarea listelor

l2 = ['a', 'b', 'c']
# print(l + l2)
# print(l)
# print(l2)

# modificarea listelor
# l2.append('d') # adauga un element
#                # la finalul listei
# print(l2)
#
# l2.insert(2, '123')
# print(l2)
#
# l2.extend([1, 2, 3])
# print(l2)

# l = []
# l = list()
# l = [1, 2, 3]
#
# l + l2
# .append, .extend, .insert
#

# pop, remove, del
#
# print(l)
# a = l.pop(3)
# print(l)
#
# l.remove(7)
# print(l)

# operatii cu liste
# print(l[::-1])
# l = l[::-1]
# print(l)
#
# # l.reverse()
# # print(l)
#
# l.sort()
# print(l)

# l = ['a', 'c', 'b']
# print(l)
# l.sort(reverse=True)
# # l = l[::-1]
# print(l)

l = list(range(20, 50))
# print(l)
#
# print(min(l))
# print(max(l))
# print(sum(l))


# operatorul "in"

print(5 in l)
print(25 in l)

# print(l[100])