def fast_mul(a, b):
    res = 0
    print("result = 0")
    while a:
        if a % 2 != 0:
            res += b
            print("result += y")
        print("y += y")
        a //= 2
        b *= 2
    print("result = " + str(res))


x, y = map(int, input().split())
print("x =", x)
print("y =", y)
fast_mul(x, y)
