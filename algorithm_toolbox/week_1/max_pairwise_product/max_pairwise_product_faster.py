# python3

from itertools import islice

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

def highest_product_of_2(list_of_ints):

    highest = max(list_of_ints[0], list_of_ints[1])

    highest_of_2 = list_of_ints[0] * list_of_ints[1]

    for current in islice(list_of_ints, 2, None):

        highest_of_2 = max(
            highest_of_2,
            current * highest)

        highest = max(highest, current)

    return highest_of_2

print(highest_product_of_2(a))
