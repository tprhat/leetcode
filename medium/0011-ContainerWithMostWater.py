"""
Container With Most Water
https://leetcode.com/problems/container-with-most-water/
"""

from typing import List


# we use 2 pointers, the furthest left and right and move the one with the smaller height towards the center
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        l, r = 0, len(height) - 1

        while l < r:
            A = min(height[l], height[r]) * (r - l)
            maxA = max(maxA, A)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxA
