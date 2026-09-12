t =(1,2,4)
res =[]
for i in range(len(t)-1,-1,-1):
    res.append(t[i])
print(tuple(res))