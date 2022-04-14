import math


def main(m, b, y):
    ans = 0
    for j in range(1, m + 1):
        ans += 1 - (j ** 2 - j ** 3 / 93) ** 3 / 25 - 18 * j

    for k in range(1, m + 1):
        for i in range(1, b + 1):
            ans -= k ** 9 + 85 * (k ** 2 / 26 - i ** 3 - y) ** 5

    return ans


print(main(6, 6, -0.28))