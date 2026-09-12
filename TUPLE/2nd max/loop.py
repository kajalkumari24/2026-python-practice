t = (1,2,9,5,4)
first = t[0]
sec= float('-inf')
for i in t:
    if i >first:
        sec = first
        first = i 
    elif i >sec and i<first:
        sec = i 
print(sec)