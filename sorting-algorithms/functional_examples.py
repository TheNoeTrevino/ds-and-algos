# 1. **`reduce`**: Applies a rolling computation to sequential pairs of values in a list.
# 2. **`all`**: Returns `True` if all elements in the iterable are true.
# 3. **`any`**: Returns `True` if any element in the iterable is true.
# 4. **`sorted`**: Returns a new sorted list from the elements of any iterable.
# 5. **`enumerate`**: Adds a counter to an iterable and returns it as an enumerate object.
# 6. **`sum`**: Sums the items of an iterable from left to right and returns the total.
# 7. **`max`**: Returns the largest item in an iterable or the largest of two or more arguments.
# 8. **`min`**: Returns the smallest item in an iterable or the smallest of two or more arguments.
#
from functools import reduce

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "2", "3", "4", "5"]


def is_even(num) -> bool:
    return num % 2 == 0


resulting_list = []


def append_evens(num):
    if is_even(num):
        resulting_list.append(num)


# map
result = list(map(lambda x: x + x, test_list))
# in respec it would be test_list.map((x) => append_evens)
map(append_evens, test_list)
print("append evenes:", resulting_list)
print("map:", result)

# filter
## with defined function
result = list(filter(is_even, test_list))
## with lambda
result = list(filter(lambda x: x % 2 == 0, test_list))
print("filter:", result)

# zip
result = list(zip(test_list, letters_list[6:]))
print("zip:", result)

# reduce
result = reduce(lambda x, y: x + y, test_list)
print("reduce:", result)

# all
result = all(is_even(num) for num in test_list)
print("all:", result)

# any
result = any(is_even(num) for num in test_list)
print("any:", result)

# sorted
result = sorted(test_list, reverse=True)
print("sorted:", result)

# enumerate
result = list(enumerate(test_list))
print("enumerate:", result)

# sum
result = sum(test_list)
print("sum:", result)

# max
result = max(test_list)
print("max:", result)

# min
result = min(test_list)
print("min:", result)
