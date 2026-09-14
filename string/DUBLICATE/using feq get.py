text = "kajal"
feq={}
for ch in text:
    feq[ch]=feq.get(ch,0)+1
    if feq[ch]>1:
        print(ch,":",feq[ch])
