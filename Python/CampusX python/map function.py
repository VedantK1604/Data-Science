# Map
# Eg.1
L = [1, 2, 3, 4, 5, 6, 7, 8]
map(lambda x: x * 2, L)  # It gives an object as an output, so we have to convert it into list.
print(list(map(lambda x: x * 2, L)))

# Eg.2
print(list(map(lambda x: x % 2 == 0, L)))
