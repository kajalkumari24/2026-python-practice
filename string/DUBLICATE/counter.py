from collections import Counter
Text = "hello"
feq = Counter(Text)
for ch , count in feq.items():
    if count>1:
        print(ch,":",count)