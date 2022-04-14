print("Умножение на 12, 4 сложения")
x = int(input())
a = x + x
b = x + a
c = b + b
print(c + c)

print("Умножение на 16, 4 сложения")

x = int(input())
a = x + x
b = a + a
c = b + b
print(c + c)

print("Умножение на 15, 3 сложения, 2 вычитания")

x = int(input())
a = x + x
b = a + a
c = b + b
d = x - c
print(c - d)

print("Умножение на 29. 6 сложений и одно вычитание")

x = int(input())
a = x + x
b = a + a
c = b + b
d = c + c
e = d + d
print(e + x - b)
