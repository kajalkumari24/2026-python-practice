text = "hello"
feq= {}
for ch in text:
  if ch in feq:
    feq[ch]+=1
  else:
    feq[ch]=1
print(feq)