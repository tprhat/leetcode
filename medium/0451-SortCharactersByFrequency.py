"""
451. Sort Characters By Frequency
https://leetcode.com/problems/sort-characters-by-frequency/
"""
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        s1 = ''
        for (i, j) in counter.most_common():
            s1 += i * j

        return s1
