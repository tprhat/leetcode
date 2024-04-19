"""
907. Sum of Subarray Minimums
https://leetcode.com/problems/sum-of-subarray-minimums/description/
"""
# https://leetcode.com/problems/sum-of-subarray-minimums/solutions/2700011/sum-of-subarray-minimums/
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        sumMins = 0

        for i in range(len(arr) + 1):

            # when i reaches the array length, it is an indication that
            # all the elements have been processed, and the remaining
            # elements in the stack should now be popped out.
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):

                # right_boundary takes equal or smaller
                # elements into account while left_boundary takes only the
                # strictly smaller elements into account
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i

                count = (mid - left) * (right - mid)

                sumMins += count * arr[mid]

            stack.append(i)

        return sumMins % 10**9 + 7