t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
res = tuple(i for i in t1 if i in t2)
print(res)