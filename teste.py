a = set()
for i in range(19):
    a.add(i)

b = set()
for i in range(8,19):
    b.add(i)

a = a.difference(b)
print(a,b)

