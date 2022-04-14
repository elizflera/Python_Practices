import math


def main(z):
    ans = 0
    n = len(z)
    for i in range(n):
        ans += (z[n - 1 - i] ** 2 - 1 - z[i // 4]) ** 7

    return ans


print(main([0.65, 0.43]))