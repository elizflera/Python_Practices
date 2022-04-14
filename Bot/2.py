import math


def main(x):
    if x < 169:
        return x ** 4 + x ** 5 + abs(x)
    elif 169 <= x < 217:
        a = 95 * math.log10(1 + x ** 3 / 33 + 20 * x * x) ** 5
        return 63 * (37 * x) ** 7 + a + 67 * (x * x - x)
    elif 217 <= x < 246:
        return x ** 3 / 9 - x ** 6 - 61 * x ** 5
    elif x >= 246:
        return 73 * x ** 6


print(main(252))
