import random
def rand_number():
    r = random.randint(1, 6)
    return r
print ("Умножение")
def fast_mul(x, y):
    sum = 0
    while x != 0:
        if x % 2 != 0:
            sum += y
        x = x >> 1
        y = y << 1
    return sum
x = rand_number()
print(x)
y = rand_number()
print(y)
print(fast_mul(x, y))

print ("Возведение в степень")
def fast_pow(a,n):
    res = a
    for i in range(n-1):
        res = fast_mul(res, a)
    return res
a = rand_number()
print(a)
n = rand_number()
print(n)
print(fast_pow(a,n))







