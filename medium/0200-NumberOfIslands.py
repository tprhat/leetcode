from typing import List


class Solution:
    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    n += 1
                    dfs(i, j)
        return n

    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n = 0
        q = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    n += 1
                    q.append((i, j))
                    while q:
                        x, y = q.pop(0)
                        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == "0":
                            continue
                        grid[x][y] = "0"
                        q.append((x - 1, y))
                        q.append((x + 1, y))
                        q.append((x, y - 1))
                        q.append((x, y + 1))
        return n
