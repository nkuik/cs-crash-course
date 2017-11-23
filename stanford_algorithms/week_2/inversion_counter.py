def merge_sort(the_list, list_size):

    temp_list = [None for _ in range(0, list_size)]
    return _merge_sort(the_list, temp_list, 0, list_size - 1)


def _merge_sort(the_list, temp_list, left_index, right_index):
    inversion_count = 0

    if right_index > left_index:
        mid = (right_index + left_index) / 2

        inversion_count = _merge_sort(the_list, temp_list, left_index, mid)
        inversion_count += _merge_sort(the_list, temp_list, mid + 1, right_index)
        inversion_count += merge(the_list, temp_list, left_index, mid + 1, right_index)

    return inversion_count


def merge(the_list, temp_list, left_index, mid, right_index):
    i = left_index
    j = mid
    k = left_index
    inversion_count = 0

    while (i <= mid - 1) and (j <= right_index):
        if the_list[i] <= the_list[j]:
            temp_list[k] = the_list[i]
            k += 1
            i += 1
        else:
            inversion_count += (mid - i)
            k += 1
            j += 1

    while i <= (mid - 1):
        temp_list[k] = the_list[i]
        k += 1
        i += 1

    while j <= right_index:
        temp_list[k] = the_list[j]
        k += 1
        j += 1

    the_list = temp_list

    return inversion_count


list_for_sorting = []
with open('input.txt', 'r') as file:
    for line in file:
        list_for_sorting.append(line.strip())

test_list = [1, 20, 6, 4, 5]
inversions = merge_sort(list_for_sorting, len(list_for_sorting))
