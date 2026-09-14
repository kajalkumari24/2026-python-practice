text = "asswrxr"
seen = set()
dublicate = set()
for ch in text:
    if ch in seen:
        dublicate.add(ch)
    else:
        seen.add(ch)
print(dublicate)