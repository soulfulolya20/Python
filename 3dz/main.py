def main(a, n, m):
    left = 0
    right = 0
    for j in range(1, n+1):
        for i in range(1, a+1):
            left += 46 * (10 + i + 26 * (j ** 2)) ** 5

    for j in range(1, a+1):
        for c in range(1, n+1):
            for k in range(1, m+1):
                right += j ** 5 - (39 * c - j ** 2) ** 2 - (k / 49 - 85) ** 7

    left -= right
    return left


if __name__ == "__main__": print(main(7, 4, 7))
