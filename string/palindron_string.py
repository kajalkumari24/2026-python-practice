s = "lajal"
1.
rev = s[::-1]
if rev == s:
    print("true")
else:
    print("false")

2.
rev = ""
for ch in s:
    rev = ch+rev
if rev == s:
    print("true")
else:
    print("false")
3.

rev = ""
i = len(s)-1
while i >=0:
    rev += s[i]
    i-=1
print(rev==s)

4.
rev = "".join(reversed(s))
print(rev==s)

5.
i = 0 
j = len(s)-1
while i <j:
    if s[i]!=s[j]:
        print("not")
        break
    i+=1
    j-=1
else:
    print("yes")