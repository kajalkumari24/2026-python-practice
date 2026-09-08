numbers = [0, 1, 0, 3, 12]
res = []
for i in numbers:
    if i!=0:
        res.append(i)
for i in numbers:
    if i==0:
        res.append(i)
print(res)