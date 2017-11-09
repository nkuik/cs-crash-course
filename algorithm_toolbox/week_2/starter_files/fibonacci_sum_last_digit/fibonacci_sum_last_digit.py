# Uses python3
import sys
from random import randint


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum_faster(num):
    if num <= 1:
        return num

    previous = 0
    current = 1
    summation = 1

    for _ in range(num - 1):

        previous, current = (current % 10), ((previous + current) % 10)
        summation += current

    return summation % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_faster(n))

# ------------------------------------------------------------------------------
# Stress Test
# ------------------------------------------------------------------------------
    # while True:
    #     example_arg = randint(1, 300)
    #     naive = fibonacci_sum_naive(example_arg)
    #     print('Naive: {}'.format(naive))
    #     faster = fibonacci_sum_faster(example_arg)
    #     print('Faster: {}'.format(faster))
    #     if naive != faster:
    #         print('Error!: Naive: {}, Faster: {}'.format(naive, faster))
