from random import randint


# currently recursing
def merge_sort(the_list):

        if len(the_list) < 2:
            return the_list, 0

        middle = int(len(the_list) / 2)

        left_sorted = merge_sort(the_list[:middle])
        right_sorted = merge_sort(the_list[middle:])
        final_merged = merge(left_sorted, right_sorted)

        return final_merged


def merge(left_list, right_list):

    if not len(left_list) or not len(right_list):
        return left_list or right_list

    result = []
    left_index = 0
    right_index = 0

    while (left_index < len(left_list) and right_index < len(right_list)):
        if left_list[left_index] < right_list[right_index]:
            result.append(left_list[left_index])
            left_index += 1
        else:
            result.append(right_list[right_index])
            right_index += 1
        if left_index == len(left_list) or right_index == len(right_list):
            result.extend(left_list[left_index:] or right_list[right_index:])
    return result


list_for_sorting = []
with open('input.txt', 'r') as file:
    for line in file:
        list_for_sorting.append(line.strip())


basic_list = [1,4,2,3]

print(merge_sort(basic_list))

