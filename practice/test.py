from typing import List


def swap(a: int, b: int, elements: List[int]):
    elements[a], elements[b] = elements[b], elements[a]


def partition(start: int, end: int, elements: List) -> int:
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


def quick_sort(start: int, end: int, elements: List) -> None:
    if start < end:
        partition_index = partition(start, end, elements)
        quick_sort(start, partition_index - 1, elements)
        quick_sort(partition_index + 1, end, elements)


tests = [[2298, 12, 3, 4, 23, 5, 3, 83], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [], [1]]
for elements in tests:
    print(elements)
    quick_sort(0, len(elements) - 1, elements)
    print(elements)
