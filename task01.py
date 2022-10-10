"""
Two Sum
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, elem in enumerate(nums):
            if elem in hashmap.keys():
                return [hashmap[elem], i]
            hashmap[target - elem] = i
