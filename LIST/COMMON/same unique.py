list1 = [1, 2, 3 , 3]
list2 = [3, 4, 5, 6, 7]
feq = {}
for i in list1:
    feq[i]= feq.get(i,0)+1
res =[]
for i in feq:
    if feq[i]==1 and i in list2:
        res.append(i)
print(res)
