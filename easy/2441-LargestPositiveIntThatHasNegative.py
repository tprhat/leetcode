from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hashmap = {}
        max_v = -1
        for i in nums:
            if i in hashmap.keys() and abs(i) > max_v:
                max_v = abs(i)
            hashmap[-i] = i

        return max_v
