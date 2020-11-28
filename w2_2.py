#
all_elem = ['a', 'b', 'c', 'd', 'e']

j = 0
for i in range(int(len(all_elem) / 2)):
    all_elem[j], all_elem[j + 1] = all_elem[j + 1], all_elem[j]
    j += 2
print(all_elem)
