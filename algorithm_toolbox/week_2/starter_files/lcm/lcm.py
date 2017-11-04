# Uses python3
import sys
from random import randint


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def lcm_faster(a, b):
    return ((a * b) // gcd_smarter(a, b))


def gcd_smarter(a, b):
    bigger = a
    smaller = b
    remainder = a % b
    while remainder != 0:
        bigger = smaller
        smaller = remainder
        remainder = bigger % smaller
    return smaller


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_faster(a, b))

# ------------------------------------------------------------------------------
# Stress Test
# ------------------------------------------------------------------------------
    # while True:
    #     first_num = randint(601, 1200)
    #     second_num = randint(1, 600)
    #     naive = lcm_naive(first_num, second_num)
    #     print(naive)
    #     faster = lcm_faster(first_num, second_num)
    #     print(faster)

    #     if naive != faster:
    #         print('ACHTUNG! Naive is: {}, Faster is: {}'.format(naive, faster))
