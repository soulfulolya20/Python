import math
from math import log


def main(y):
    if y < 128:
        return 57 * (y ** 2) - (9 + (y ** 3 / 62)) ** 7
    if 128 <= y < 184:
        return 7 * (y ** 2) - ((13 * (y ** 3) - 53 * y - 89) ** 7 / 33) \
               - (57 * y - 3 * (y ** 3)) ** 3
    if 184 <= y < 273:
        return 93 * log(y) ** 3 - (math.ceil(y ** 2)) ** 6
    if y >= 273:
        return y ** 3 - (y - 7 - y ** 3) ** 7


if __name__ == "__main__": print(main(243))
