numbers = [1, 2, 2, 3, 4, 4, 5]
feq={}
for i in numbers:
    feq[i]=feq.get(i,0)+1
for key , value in feq.items():
    if value==1:
        print(key)