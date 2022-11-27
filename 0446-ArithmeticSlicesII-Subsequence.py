"""
446. Arithmetic Slices II - Subsequence
https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/
"""
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/solutions/2852788/python3-dp-explained-o-n-2/
from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))]
        res = 0
        print(dp)
        for i in range(len(nums)):
            for j in range(i):
                # number of elements before j in the arithmetic subsequence that has nums[j]-nums[i] as difference
                dif = nums[j] - nums[i]
                res += dp[j][dif]
                # Increase the number of elements in arithmetic subsequence at i with this dif
                dp[i][dif] += dp[j][dif] + 1

        return res


print(Solution.numberOfArithmeticSlices(Solution(), nums=[2, 4, 6, 8, 10]))
