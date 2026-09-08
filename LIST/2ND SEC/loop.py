n = [10, 25, 7, 40, 15]
lar=float('-inf')
slar=float('-inf')
for i in n:
    if i>lar:
        slar=lar
        lar=i
    elif i>slar and i!=lar:
        slar=i
print(slar)