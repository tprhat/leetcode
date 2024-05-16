"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
"""

from typing import List


# zip(*strs) Iterate over all words in parallel, producing tuples with a letter from each one.
# It will stop iteration on the shortest word.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        for i in zip(*strs):
            s = set(i)
            if len(s) == 1:
                prefix.append(s.pop())
            else:
                break
        return "".join(prefix)
