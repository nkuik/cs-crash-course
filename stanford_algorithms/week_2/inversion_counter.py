def merge_sort(the_list):

        if len(the_list) < 2:
            return the_list

        middle = len(the_list)//2

        left = the_list[middle:]
        right = the_list[:middle]

        return merge(merge_sort(left), merge_sort(right))


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
            break
    return result



print(merge_sort([3, 95, 237, 2398, 982, 2350, 2816]))
