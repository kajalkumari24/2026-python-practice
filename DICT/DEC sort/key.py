data = {
    "banana": 3,
    "apple": 5,
    "cherry": 2
}
res = dict(sorted(data.items(),reverse = True))
print(res)