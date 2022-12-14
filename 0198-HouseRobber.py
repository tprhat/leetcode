"""
198. House Robber
https://leetcode.com/problems/house-robber/
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0

        for i in nums:
            print(i)

            last, now = now, max(last + i, now)
            print(last, now)

        return now
