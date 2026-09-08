n = [1, 2, 2, 3, 4, 4, 5]
feq={}
for i in n:
    feq[i]=feq.get(i,0)+1
res= []
for i  in n:
    if i not in res:
        res.append(i)
print(res)