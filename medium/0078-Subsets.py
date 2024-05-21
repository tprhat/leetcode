import itertools
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums) + 1):
            for elem in itertools.combinations(nums, i):
                res.append(list(elem))
        return res
