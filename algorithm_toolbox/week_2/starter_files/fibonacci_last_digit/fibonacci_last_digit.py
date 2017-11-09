# Uses python3
import sys
from random import randint

# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current = 1

#     for _ in range(n - 1):

#         previous, current = current, previous + current

#     return current % 10


def get_fibonacci_last_digit(num):
    if num <= 1:
        return num

    previous = 0
    current = 1

    for _ in range(num - 1):

        previous, current = (current % 10), ((previous + current) % 10)

    return current


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))


# ------------------------------------------------------------------------------
# Stress Test
# ------------------------------------------------------------------------------
    # while True:
    #     example_arg = randint(1, 300)
    #     naive = get_fibonacci_last_digit_naive(example_arg)
    #     print('Naive: {}'.format(naive))
    #     faster = get_fibonacci_last_digit(example_arg)
    #     print('Faster: {}'.format(faster))
    #     if naive != faster:
    #       print('Error!: Naive: {}, Faster: {}'.format(naive, faster))
