from random import randint

def merge_sort(the_list):

        if len(the_list) < 2:
            return the_list

        middle = len(the_list)//2

        left = the_list[middle:]
        right = the_list[:middle]

        return merge(merge_sort(left), merge_sort(right))


inversion_counter = 0

def merge(left_list, right_list):

    if not len(left_list) or not len(right_list):
        return left_list or right_list

    result = []
    left_index = 0
    right_index = 0

    while (len(result) < (len(left_list) + len(right_list))):
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

the_list = merge_sort(list_for_sorting)


# while True:
#     list_for_sorting = [randint(0, 100000) for _ in range(1,100)]

#     merge_sorted = merge_sort(list_for_sorting)
#     python_sorted = sorted(list_for_sorting)

#     if merge_sorted != python_sorted:
#         print('Shit, they\'re unequal')
#     else:
#         print('Equal!')
