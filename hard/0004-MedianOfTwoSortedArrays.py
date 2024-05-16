"""
Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        r = math.ceil(l / 2)
        pair = False
        if l % 2 == 0:
            pair = True
            r = l / 2 + 1
        first, second = 0, 0
        for i in range(0, int(r)):
            first = second
            arr1 = nums1[0] if len(nums1) > 0 else None
            arr2 = nums2[0] if len(nums2) > 0 else None
            if arr1 is not None and arr2 is not None:
                if arr1 < arr2:
                    second = arr1
                    nums1.pop(0)
                else:
                    second = arr2
                    nums2.pop(0)
            if arr1 is not None and arr2 is None:
                second = arr1
                nums1.pop(0)
            if arr1 is None and arr2 is not None:
                second = arr2
                nums2.pop(0)
            if i == r - 1:
                if pair:
                    return (first + second) / 2
                else:
                    return second
