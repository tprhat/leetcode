"""
947. Most Stones Removed with Same Row or Column
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
"""

from typing import List
from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        groupByX = defaultdict(list)
        groupByY = defaultdict(list)

        for i, (x, y) in enumerate(stones):
            groupByX[x].append(i)
            groupByY[y].append(i)

        disjointSet = 0
        visited = set()

        for i in range(n):
            if i in visited:
                continue
            stack = [i]
            disjointSet += 1

            while stack:
                curr = stack.pop()
                visited.add(curr)
                x, y = stones[curr]

                for next_i in groupByX[x]:
                    if next_i not in visited:
                        stack.append(next_i)

                for next_j in groupByY[y]:
                    if next_j not in visited:
                        stack.append(next_j)

        return n - disjointSet


print(Solution.removeStones(Solution(), [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
