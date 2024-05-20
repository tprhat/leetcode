import itertools
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums) + 1):
            for comb in itertools.combinations(nums, i):
                total_comb = 0
                for c in comb:
                    total_comb ^= c
                total += total_comb
        return total
