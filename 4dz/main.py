import math


def main(n):
    if n == 0:
        return 0.09
    if n == 1:
        return 0.23
    if n >= 2:
        return 1 - (main(n - 2)) / 46 - math.log2(88 - (main(n - 1)) - 44 *
                                                  (main(n - 2)) ** 3) ** 2


if __name__ == "__main__": print(main(9))
