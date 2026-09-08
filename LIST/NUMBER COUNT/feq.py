numbers = [1, 2, 2, 3, 3, 3, 4]
feq={}
for i in numbers:
    feq[i]= feq.get(i,0)+1
print(feq)