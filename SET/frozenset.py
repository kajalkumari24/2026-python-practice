#after frozenset we can not change the set, it is immutable
s = frozenset([1, 2, 3])
# s.add(4)  # frozenset' object has no attribute 'add'
print(s)