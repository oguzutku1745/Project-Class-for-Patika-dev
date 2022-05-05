liste = [[1, 2], [3, 4], [5, 6, 7]]
a = []
for i in liste[::-1]:
    a.append(i[::-1])

print(a)
