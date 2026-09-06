s ="Kajal"
1 . print(s[::-1])

2.
rev = ""
i = len(s)-1
while i>=0:
    rev += s[i]
    i-=1
print(rev)

3.
rev = "".join(reversed(s))
print(rev)

4.
rev = ""
for ch  in s :
    rev = ch+rev
print(rev)

