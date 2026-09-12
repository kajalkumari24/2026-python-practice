t =(1,2,1,1,6)
feq = {}
for i in t:
    feq[i]=feq.get(i,0)+1
print(1 ,"count =", feq[1])