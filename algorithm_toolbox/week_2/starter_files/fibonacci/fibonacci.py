# Uses python3
def calc_fib(num):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for i in range(num - 1):
        previous, current = current, previous + current

    return current


n = int(input())
print(calc_fib(n))
