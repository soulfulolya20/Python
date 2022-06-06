# import math
#
#
# def eval_second(m, a, b, z):
#     sum_b = 0
#     sum_m = 0
#     for j in range(1, m + 1):
#         for i in range(1, b + 1):
#             proizv = 1
#             for c in range(1, a + 1):
#                 proizv *= ((21 * z + j ** 2) ** 3) - 66 * (i ** 6) - 13 * c
#             sum_b += proizv
#
#     for i in range(1, a + 1):
#         for k in range(1, m + 1):
#             sum_m += (69 * ((95 * (k ** 2)) ** 3)) - 91 * (i ** 5) - (math.cos(i)) ** 7
#     return sum_m + sum_b
#
#
# print("{:.2e}".format(eval_second(6, 6, 3, 0.92))) сумма сумма произведение
import math


# def eval(a, b, p):
#     proizv = 1
#     sum_2 = 0
#     for c in range(1, b + 1):
#         sum_a = 0
#         for j in range(1, a + 1):
#             sum_a += (96 * (c ** 2 - 55 * (j ** 3)) - (8 + (j ** 3)) ** 2)
#         proizv *= sum_a
#
#     for i in range(1, b + 1):
#         for c in range(1, a + 1):
#             sum_2 += ((81 + p / 32) ** 4) / 17 + math.ceil(p ** 3 - 1 - i) + 73 * (c ** 2)
#     return proizv + sum_2
#
# print("{:.2e}".format(eval(8, 2, -0.37))) произведение сумма округление в большую сторону