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
        if the_list[i] < the_list[j]:
            temp_list[k] = the_list[i]
            k += 1
            i += 1
        else:
            temp_list[k] == the_list[j]
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

    the_list = [temp_list[i] for i in range(0, len(the_list))]

    return inversion_count


list_for_sorting = []
with open('input.txt', 'r') as file:
    for line in file:
        list_for_sorting.append(line.strip())

test_list = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
inversions = merge_sort(test_list, len(test_list))

print(inversions)


def merge_list(left, right):
    result = []
    i,j = 0,0
    inv_count = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif right[j] < left[i]:
            result.append(right[j])
            j += 1
            inv_count += (len(left)-i)
    result += left[i:]
    result += right[j:]
    return result, inv_count


def sort_and_count(array):
    if len(array) < 2:
        return array, 0

    middle = len(array) / 2

    left, inv_left = sort_and_count(array[:middle])
    right, inv_right = sort_and_count(array[middle:])
    merged, count = merge_list(left,right)

    count += (inv_left + inv_right)

    return merged, count




list_for_sorting = []
with open('input.txt', 'r') as file:
    for line in file:
        list_for_sorting.append(line.strip())


basic_list = [5,4,3,2,1]

sorted_list, count = sort_and_count(list_for_sorting)
print(count)




# while True:
#     list_for_sorting = [randint(0, 100000) for _ in range(1,100)]

#     merge_sorted = merge_sort(list_for_sorting)
#     python_sorted = sorted(list_for_sorting)

#     if merge_sorted != python_sorted:
#         print('Shit, they\'re unequal')
#     else:
#         print('Equal!')
