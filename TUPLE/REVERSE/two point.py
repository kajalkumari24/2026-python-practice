t = (1,2,4)
t = list(t)
l = 0
r = len(t)-1
while l<r:
    t[l],t[r]=t[r],t[l]
    r-=1
    l+=1
print(tuple(t))