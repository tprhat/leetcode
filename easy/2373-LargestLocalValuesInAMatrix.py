from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = [[0] * (len(grid) - 2) for _ in range(len(grid) - 2)]

        for i in range(0, len(grid) - 2):
            for j in range(0, len(grid) - 2):
                res[j][i] = max(
                    [grid[k][l] for k in range(j, j + 3) for l in range(i, i + 3)]
                )

        return res
