from datetime import datetime


def bubble_sort(elements: list[dict], key):
    start = datetime.now()

    size = len(elements)
    for i in range(size - 1):

        print(f"Iteration {i+1}: ")
        swapped = False

        for j in range(size - 1 - i):
            if elements[j][key] > elements[j + 1][key]:

                # swapping
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp

                swapped = True

            print(elements)

        if not swapped:
            break

    end = datetime.now()

    print(f"start: {start}")
    print(f"end: {end}")


elements = [
    {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
    {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
    {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
    {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
]

print("Starting list")
print(elements)
bubble_sort(elements, key="name")

# .8 sec with filtering already sorted
# .8 sec with filtering already sorted but not the count
# 40 sec with filtering the count
# 140 witout filtering the count
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# elements = [5, 1, 89, 23, 13, 9, 281, 22, 2, 0, 98398]
# elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(1000):
#     elements.append(i)
#
