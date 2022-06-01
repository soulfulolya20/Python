import math


def main(z):
    answer = 0
    left = math.sqrt(((62 * z - 85 * (z ** 2)) ** 6) /
                     (70 * ((math.floor(1 + 16 * z)) ** 4) + (z ** 3) / 15))

    right = math.sqrt(65 * (77 * (z ** 3)) ** 7 + 29 * (46 * (z ** 3)) ** 6)

    answer = left + right

    return answer

print(main(0.37))
