"""
15. 3Sum
https://leetcode.com/problems/3sum/
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        if len(nums) < 3:
            return []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                value = nums[i] + nums[left] + nums[right]
                if value > 0:
                    right -= 1
                elif value < 0:
                    left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
        return results


print(Solution.threeSum(Solution(), [-1, 0, 1, 2, -1, -4]))
