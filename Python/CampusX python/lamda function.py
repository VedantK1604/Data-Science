# Lambda functions

"""Syntax= lamda inputs: expression"""
x = lambda x: print(x ** 2)
x(9)

a = lambda x, y: print(x + y)
a(4, 5)

b = lambda x: x[0] == 'a'
print(b("apple"))

c = lambda x: "Even" if x % 2 == 0 else "Odd"
print(c(3))
