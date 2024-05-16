"""
2225. Find Players With Zero or One Losses
https://leetcode.com/problems/find-players-with-zero-or-one-losses/
"""

from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        outcomes = defaultdict(int)
        for match in matches:
            if match[0] not in outcomes:
                outcomes[match[0]] = 0
            outcomes[match[1]] += 1
        zero_losses = []
        one_loss = []
        for k, v in outcomes.items():
            if v == 0:
                zero_losses.append(k)
            elif v == 1:
                one_loss.append(k)

        return [sorted(zero_losses), sorted(one_loss)]


print(
    Solution.findWinners(
        Solution(),
        matches=[
            [1, 3],
            [2, 3],
            [3, 6],
            [5, 6],
            [5, 7],
            [4, 5],
            [4, 8],
            [4, 9],
            [10, 4],
            [10, 9],
        ],
    )
)
