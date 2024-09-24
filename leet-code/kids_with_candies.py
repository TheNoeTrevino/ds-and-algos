from typing import List


def kidsWithCandiesFunctional(candies: List[int], extraCandies: int) -> List[bool]:
    bully = max(candies)
    return list(map(lambda k: k + extraCandies >= bully, candies))


print(kidsWithCandiesFunctional([2, 3, 5, 1, 3], 3))


def kidsWithCandiesStandard(candies: List[int], extraCandies: int) -> List[bool]:
    bully = max(candies)
    results = []
    for kid in candies:
        if kid + extraCandies >= bully:
            results.append(True)
        else:
            results.append(False)
    return results


print(kidsWithCandiesStandard([2, 3, 5, 1, 3], 3))


def kidsWithCandiesStandardConsice(candies: List[int], extraCandies: int) -> List[bool]:
    bully = max(candies)
    results = []
    for kid in candies:
        results.append(kid + extraCandies >= bully)
    return results


print(kidsWithCandiesStandardConsice([2, 3, 5, 1, 3], 3))
