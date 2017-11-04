# Uses python3
import sys
from random import randint

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_smarter(a, b):
    bigger = a
    smaller = b
    remainder = a % b
    while remainder != 0:
        bigger = smaller
        smaller = remainder
        remainder = bigger % smaller
    return smaller


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_smarter(a, b))


# ------------------------------------------------------------------------------
# Stress Test
# ------------------------------------------------------------------------------
    # while True:
    #     first_num = randint(601, 1200)
    #     print(first_num)
    #     second_num = randint(1, 600)
    #     print(second_num)
    #     naive = gcd_naive(first_num, second_num)
    #     smarter = gcd_smarter(first_num, second_num)

    #     if naive != smarter:
    #         print('ACHTUNG! Naive is: {}, Smarter is: {}'.format(naive, smarter))
