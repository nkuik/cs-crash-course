from random import randrange, randint
import click
import copy


def first(lst, start, end):
    return start


def last(lst, start, end):
    return end


def median(lst, start, end):
    mean = (start + end) // 2
    if lst[start] < lst[end]:
        return end if lst[end] < lst[mean] else mean
    else:
        return start if lst[start] < lst[mean] else mean


def _quick_sort(lst, start, end, pivot_selector):
    count = 0
    if start < end:
        new_pivot, count = partition(lst, start, end, pivot_selector)
        count += _quick_sort(lst, start, new_pivot - 1, pivot_selector)
        count += _quick_sort(lst, new_pivot + 1, end, pivot_selector)
    return count


def swap(lst, index1, index2):
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp


def partition(lst, start, end, pivot_selector):
    count = 0
    i = start
    pivot_index = pivot_selector(lst, start, end)
    pivot = lst[pivot_index]
    lst[start], lst[pivot_index] = lst[pivot_index], lst[start]
    for j in range(start + 1, end + 1):
        count += 1
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i], lst[start] = lst[start], lst[i]
    return i, count


@click.command()
@click.argument('provided_list', type=click.File('r'))
def quick_sort(provided_list):
    list_for_sorting = []
    for line in provided_list:
        list_for_sorting.append(line.strip())

    start_list = copy.deepcopy(list_for_sorting)
    end_list = copy.deepcopy(list_for_sorting)
    median_list = copy.deepcopy(list_for_sorting)

    start_count = _quick_sort(
        start_list, 0, len(list_for_sorting) - 1, first)

    end_count = _quick_sort(
        end_list, 0, len(list_for_sorting) - 1, last)

    median_count = _quick_sort(
        median_list, 0, len(list_for_sorting) - 1, median)

    assert start_list == sorted(list_for_sorting)
    assert end_list == sorted(list_for_sorting)
    assert median_list == sorted(list_for_sorting)

    print(f'Start: {start_count}, End: {end_count}, Median: {median_count}')

    # ======================================
    # Stress Test
    # ======================================

    # while True:
    #     list_for_sorting = [randint(0, 100000) for _ in range(1,100)]

    #     copied_list = copy.deepcopy(list_for_sorting)

    #     _quick_sort(copied_list, 0, len(list_for_sorting) - 1, first)
    #     python_sorted = sorted(list_for_sorting)

    #     if copied_list != python_sorted:
    #         print('Shit, they\'re unequal')
    #     else:
    #         print('Equal!')


if __name__ == '__main__':
    quick_sort()

