from math import *
from random import randint


def simple_karatsuba(x, y):
    return x * y

def karatsuba(x, y):
    B = 10

    if x < 10 or y < 10:
        return x * y

    else:
        m = max(int(log10(x)+1), int(log10(y)+1))

        if m % 2 != 0:
            m -= 1
        m_2 = int(m/2)

        a, b = divmod(x, B**m_2)
        c, d = divmod(y, B**m_2)

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

        return ((ac * (10**m)) + bd + ((ad_plus_bc) * (10**m_2)))


if __name__ == '__main__':

    while True:

        a = 3141592653589793238462643383279502884197169399375105820974944592
        b = 2718281828459045235360287471352662497757247093699959574966967627

        simple = simple_karatsuba(a, b)
        recurse = karatsuba(a, b)

        print(simple)
        print(recurse)

        if simple != recurse:
            print(f'Not equal with these: {a}, {b}')
