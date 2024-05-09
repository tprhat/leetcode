from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total = 0
        for i, x in enumerate(happiness):
            if i == k:
                break
            total += max(0, x - i)
        return total
