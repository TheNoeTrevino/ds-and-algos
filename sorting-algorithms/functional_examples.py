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
# in java/js/ts and other languages it would be test_list.map((x) => append_evens)
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

# REDUCE
# A bit more complicated. When no initial value is provided the first element of
# the array is used as the inital value, then begins to accumalate.
# x is the accumalator, and y is the iterator
result = reduce(lambda x, y: x + y, test_list)
print("reduce with no inital value:", result)
# if you add an inital value, instead of starting with the first element, it
# will add the first element to the intial value, and continue
inital_value = 50
result = reduce(lambda x, y: x + y, test_list, inital_value)
print("reduce with the inital value of 50:", result)

# ALL
# checks if a condition returns true for all the iteration in a list
# note: works with splicing
result = all(is_even(num) for num in test_list)
print("all named function:", result)
# if wanting to use a lambda use it this way to avoid type error
# above is probably better though
result = all((lambda num: num % 2 == 0)(num) for num in test_list)
print("all lambda function :", result)

# any
# similar to all, but check if any of them hold true to the function instead
result = any(is_even(num) for num in test_list)
print("any:", result)

# sorted sorts a list, least to greatest. Use reverse if desired
result = sorted(test_list, reverse=True)
print("sorted:", result)

# enumerate
# returns a tuple of the indicies, and the value. (0, 1) etc...
# really good for leet code where both the value and the index are used. will make
# those algorithmic problems more managable
# even in two sum, this is super helpful
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

test_dictionary = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

# NOTE: with max, min, sorted, and some others...
# we can use the key with a lambda function to decide what is the attribute
# that is being sorted upon. Good for dictionaries, and data structures where
# something other than the default value is what we want to be judged
result = max(test_dictionary, key=lambda x: x["age"])  # can be name, etc...
print("max by age:", result)
