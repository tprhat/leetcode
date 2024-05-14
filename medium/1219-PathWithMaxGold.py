from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(grid)
        m = len(grid[0])
        maxGold = 0

        def dfs(visited, x, y):
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0 or visited[x][y]:
                return 0

            visited[x][y] = True

            nextMax = max(
                dfs(visited, x + moves[0][0], y + moves[0][1]),
                dfs(visited, x + moves[1][0], y + moves[1][1]),
                dfs(visited, x + moves[2][0], y + moves[2][1]),
                dfs(visited, x + moves[3][0], y + moves[3][1]),
            )

            visited[x][y] = False
            return grid[x][y] + nextMax

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    visited = [[False for p in range(m)] for q in range(n)]
                    maxGold = max(maxGold, dfs(visited, i, j))

        return maxGold
