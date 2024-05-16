from functools import reduce
from typing import List


# For each different bit between the bitwise XOR of elements of the original array and k
# we have to flip exactly one bit of an element in nums to make that bit equal
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = reduce(lambda x, y: x ^ y, nums)
        res = res ^ k
        return bin(res).count("1")
