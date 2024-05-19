from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        deltas = []
        for i in nums:
            deltas.append((i ^ k) - i)

        deltas.sort(reverse=True)
        total = sum(nums)
        best = total

        i = 0
        while i + 1 < len(nums):
            total += deltas[i] + deltas[i + 1]
            best = max(total, best)
            i += 2
        return best
