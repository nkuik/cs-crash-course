from random import randrange, randint


def partition(lst, start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    store_index = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    lst[store_index], lst[end] = lst[end], lst[store_index]
    return store_index


def quick_sort(lst, start, end):
    if start >= end:
        return lst
    pivot = start
    new_pivot = partition(lst, start, end, pivot)
    quick_sort(lst, start, new_pivot - 1)
    quick_sort(lst, new_pivot + 1, end)


def sort(lst):
    quick_sort(lst, 0, len(lst) - 1)
    return lst


while True:
    list_for_sorting = [randint(0, 100000) for _ in range(1,100)]

    quick_sorted = sort(list_for_sorting)
    python_sorted = sorted(list_for_sorting)

    if quick_sorted != python_sorted:
        print('Shit, they\'re unequal')
    else:
        print('Equal!')
