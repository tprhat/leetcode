from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = (1 << n - 1) * m

        for j in range(1, n):
            curr = sum(grid[i][j] == grid[i][0] for i in range(m))
            res += max(curr, m - curr) * (1 << n - 1 - j)
        return res
