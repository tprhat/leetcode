"""
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dist = {}
        for i in range(n):
            if nums[i] not in dist.keys():
                dist[nums[i]] = i
            else:
                if i - dist[nums[i]] <= k:
                    return True
                dist[nums[i]] = i
        return False
