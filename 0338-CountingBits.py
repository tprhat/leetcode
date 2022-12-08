"""
338. Counting Bits
https://leetcode.com/problems/counting-bits/
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        while len(res) <= n:
            res += [i + 1 for i in res]
            # print(res)
        return res[:n + 1]
