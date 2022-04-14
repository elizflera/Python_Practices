import math


def main(n):
    if n == 0:
        return 0.50
    elif n == 1:
        return 0.95
    elif n >= 2:
        return (main(n - 2) - main(n - 1) ** 2) ** 2


print(main(4))