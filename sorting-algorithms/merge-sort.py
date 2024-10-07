from typing import List


def merge(array_a, array_b):
    i, j = 0, 0
    sorted_array = []

    while len(array_a) > i and len(array_b) > j:
        if array_a[i] < array_b[j]:
            sorted_array.append(array_a[i])
            i += 1
        else:
            sorted_array.append(array_b[j])
            j += 1

    while len(array_a) > i:
        sorted_array.append(array_a[i])
        i += 1

    while len(array_b) > j:
        sorted_array.append(array_b[j])
        j += 1

    return sorted_array


def merge_sort(array: List):
    if len(array) <= 1:

        print(array)
        return array

    mid = len(array) // 2

    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))


test_array = [1, 2, 3, 4, 5, 6]
test_array2 = [6, 2, 4, 6, 1, 3, 79, 45, 2, 234, 0]
print("array 1 results: ")
print(merge_sort(test_array))
print("array 2 results: ")
print(merge_sort(test_array2))
