def return_sum(func, L):
    result = 0
    for i in L:
        if func[i]:
            result += i
    return result

L = [2, 3, 5, 7, 9, 6, 12, 24, 46, 69, 72]

x = lambda x: x % 2 == 0
y = lambda y: y % 2 != 0
z = lambda z: z % 3 == 0

print(return_sum(x, L))
print(return_sum(y, L))
print(return_sum(z, L))
