"""
2256. Minimum Average Difference
https://leetcode.com/problems/minimum-average-difference/
"""

from math import floor
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        min_avg_diff = 1e15
        min_avg_diff_id = None
        prefix_sum = 0
        sum_nums = sum(nums)

        for i in range(len(nums)):
            left = floor((prefix_sum + nums[i]) / (i + 1))
            if len(nums) - i - 1 != 0:
                right = floor((sum_nums - prefix_sum - nums[i]) / (len(nums) - i - 1))
            else:
                right = 0
            prefix_sum += nums[i]

            res = abs(left - right)
            if res == 0:
                return i
            if res < min_avg_diff:
                min_avg_diff = res
                min_avg_diff_id = i
        return min_avg_diff_id


print(Solution.minimumAverageDifference(Solution(), nums=[0, 1, 0, 1, 0, 1]))
