import functools

L = [12, 34, 56, 11, 21, 58]
print(functools.reduce(lambda x, y: x if x > y else y, L))
