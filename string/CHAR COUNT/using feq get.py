text = "hello"
feq= {}
for ch in text:
  feq[ch] = feq.get(ch,0)+1
print(feq)