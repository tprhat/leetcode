"""
1657. Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close/description/
"""

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return all(
            x == y
            for x, y in zip(
                sorted(list(Counter(word1).values())),
                sorted(list(Counter(word2).values())),
            )
        ) and set(word1) == set(word2)
