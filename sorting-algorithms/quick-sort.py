from typing import List


# lomuto partition
# super cool pythonic way to swap
def swap(a: int, b: int, arr: List[int]):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def partition(start: int, end: int, elements: List):
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


def quick_sort(start, end, elements: List):
    if start < end:
        pi = partition(start, end, elements)
        # left partition
        quick_sort(start, pi - 1, elements)
        # right partition
        quick_sort(pi + 1, end, elements)
        # partition(start, end, elements)


elements = [12, 3, 2, 34, 4232, 12, 54, 98, 678, 87, 1]
print(elements)
quick_sort(0, len(elements) - 1, elements)
print(elements)
