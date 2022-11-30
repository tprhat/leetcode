"""
1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/
"""
from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash = defaultdict(int)  # or use Counter - possibly better?
        for i in arr:
            hash[i] += 1
        return len(hash) == len(set(hash.values()))
