text = "hello"
seen = set()
res = ""
for ch in text:
    if ch not in seen:
        seen.add(ch)
        res+=ch
print(res)
