from typing import List


def swap(a, b, elements: List):
    elements[a], elements[b] = elements[b], elements[a]


def quick_sort(start, end, elements):
    if start < end:
        split = partition(start, end, elements)
        quick_sort(start, split - 1, elements)
        quick_sort(split + 1, end, elements)


def partition(start, end, elements: List):
    pivot_index = start
    pivot = elements[pivot_index]

    # in this while loop we, are make sure everthing to right of the pivot is greater and everything to the left is less
    while start < end:
        # mark one greater that the pivot
        while start < len(elements) - 1 and elements[start] <= pivot:
            start += 1

        # mark one less that the pivot
        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


elements = [40, 2, 34, 5, 8, 23, 1, 90]
quick_sort(0, len(elements) - 1, elements)
print(elements)
