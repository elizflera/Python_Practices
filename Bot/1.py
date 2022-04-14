import math


def main(y):
    a = y ** 3 / (y ** 7 - 17)
    b = 35 * math.sin(99 * y ** 3 - 44 * y ** 2) ** 4 / y ** 7
    return a + b


print(main(-0.86))