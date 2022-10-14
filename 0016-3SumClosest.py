"""
3Sum Closest
https://leetcode.com/problems/3sum-closest/
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = None
        closest_sum = 10e4
        nums = sorted(nums)
        for i in range(0, len(nums) - 1):

            if nums[i] == nums[i - 1] and i > 0:
                continue

            lower = i + 1
            upper = len(nums) - 1

            while lower < upper:
                tsum = nums[i] + nums[lower] + nums[upper]
                if tsum == target:
                    return tsum
                if abs(tsum - target) < closest_sum:
                    closest = tsum
                    closest_sum = abs(tsum - target)

                if tsum > target:
                    upper -= 1

                if tsum < target:
                    lower += 1

        return closest


print(Solution.threeSumClosest(Solution(), [1, 1, 1, 1], 0))
