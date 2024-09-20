from typing import List


def twoSum(nums: List[int], target: int):
    # first off we have to understand that if there is a complement, then the complement would appear later.
    # we are adding the index because that is what teh problem was asking for
    # if it was just answering if it was there at all, we could probably use an array, and just return true if it is there

    # number: index
    num_map = {}
    for i, num in enumerate(nums):  # this turns (index, num) for each num
        # find complement
        complement = target - num
        # see if complement is in our map so far, if it isnt it could possibly be the answer later on
        if complement in num_map:
            return [num_map[complement], i]
        # since it could be there later on, add it to our dictionary
        num_map[num] = i


my_dictionary = {
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

solution = twoSum([2, 7, 11, 15], 9)
print(solution)
