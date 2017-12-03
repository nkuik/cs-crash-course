from random import randrange, randint
import click
import copy


SORT_TYPE = None

def _quick_sort(lst, start, end):
    comparisons = 0
    if start <= end:
        if SORT_TYPE == 'start':
            pivot = start
        if SORT_TYPE == 'end':
            pivot = end
        if SORT_TYPE == 'median':
            pivot = median(lst, start, end, (start + end) // 2)
        new_pivot, comparisons = partition(lst, start, end, pivot)
        comparisons += _quick_sort(
            lst, start, new_pivot - 1)
        comparisons += _quick_sort(
            lst, new_pivot + 1, end)
    return comparisons


def partition(lst, start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    count = end - start
    store_index = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    lst[store_index], lst[end] = lst[end], lst[store_index]
    return store_index, count


def median(lst, start, end, mean):
  if lst[start] < lst[end]:
    return end if lst[end] < lst[mean] else mean
  else:
    return start if lst[start] < lst[mean] else mean


@click.command()
@click.argument('provided_list', type=click.File('r'))
def quick_sort(provided_list):
    global SORT_TYPE
    list_for_sorting = []
    for line in provided_list:
        list_for_sorting.append(line.strip())
    SORT_TYPE = 'start'
    start_list = copy.deepcopy(list_for_sorting)
    start = _quick_sort(
        start_list, 0, len(list_for_sorting) - 1)
    SORT_TYPE = 'end'
    end_list = copy.deepcopy(list_for_sorting)
    end = (_quick_sort(
        end_list, 0, len(list_for_sorting) - 1))
    SORT_TYPE = 'median'
    median_list = copy.deepcopy(list_for_sorting)
    median = (_quick_sort(
        median_list, 0, len(list_for_sorting) - 1))
    print(f'Start: {start}, End: {end}, Median: {median}')


if __name__ == '__main__':
    quick_sort()

# ======================================
# Stress Test
# ======================================
# while True:
#     list_for_sorting = [randint(0, 100000) for _ in range(1,100)]

#     _quick_sorted = sort(list_for_sorting)
#     python_sorted = sorted(list_for_sorting)

#     if _quick_sorted != python_sorted:
#         print('Shit, they\'re unequal')
#     else:
#         print('Equal!')
