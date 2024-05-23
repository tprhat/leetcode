import collections
from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N: int = len(nums)
        
        def recurse(index: int, counter: collections.Counter):
            if index == N:
                return 1
            
            total = 0
            
            total += recurse(index + 1, counter)
            if counter[nums[index] - k] == 0 and counter[nums[index] + k] == 0:
                counter[nums[index]] += 1
                total += recurse(index + 1, counter)
                counter[nums[index]] -= 1
            return total
        return recurse(0, collections.Counter()) - 1