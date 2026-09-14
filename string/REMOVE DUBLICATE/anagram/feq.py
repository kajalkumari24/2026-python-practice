str1 = "listen"
str2 = "silent"
if len(str1)!=len(str2):
    print("not anagram")
else:
    feq={}
    for ch in str1:
        feq[ch]=feq.get(ch,0)+1

    for ch in str2:
        feq[ch] = feq.get(ch , 0)-1
    if all(value ==0 for value in feq.value()):
        print("anagram")
    else:
        print("not")
