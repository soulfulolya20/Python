from math import ceil, atan


def main(z):
    n = [0] * (len(z) + 1)
    answer = 0
    for i in range(len(n)):
        if i != 0:
            n[i] = z[i - 1]
    for i in range(1, len(z) + 1):
        answer += atan(40 - n[len(z) + 1 - i] ** 2 - n[ceil(i / 4)]
                       ** 3) ** 3
    return answer


if __name__ == "__main__": print(main([0.29, -0.24, -0.34, 0.4, -0.14]))
