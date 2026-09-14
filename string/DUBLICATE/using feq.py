text = "jaajr"
feq = {}
for ch in text:
    if ch in feq:
        feq[ch]+=1
    else:
        feq[ch]=1
for ch , count in feq.items():
    if count>1:
        print(ch,":",count)