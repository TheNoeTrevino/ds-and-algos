from typing import List


def test_radix_sort():
    assert radix_sort([]) == []
    assert radix_sort([5]) == [5]
    assert radix_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert radix_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert radix_sort([3, 1, 4, 5, 2]) == [1, 2, 3, 4, 5]
    assert radix_sort([4, 2, 4, 3, 1, 2]) == [1, 2, 2, 3, 4, 4]
    assert radix_sort([123, 456, 789, 101112, 131415]) == [
        123,
        456,
        789,
        101112,
        131415,
    ]
    assert radix_sort([1, 1000, 10, 100, 10000]) == [1, 10, 100, 1000, 10000]


# Assuming radix_sort is the function to be tested
def radix_sort(arr: List[int]) -> List[int]:
    # Implementation of radix sort
    return []
