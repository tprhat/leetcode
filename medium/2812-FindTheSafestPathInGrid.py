import collections
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        INF = 10**20

        safety = [[INF] * n for _ in range(n)]
        q = collections.deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    safety[i][j] = 0
                    q.append((0, i, j))

        while len(q) > 0:
            d, x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and safety[nx][ny] == INF:
                    safety[nx][ny] = d + 1
                    q.append((d + 1, nx, ny))

        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        q = collections.deque()
        q.append((safety[0][0], 0, 0))

        while len(q) > 0:
            d, x, y = q.popleft()

            if x == n - 1 and y == n - 1:
                return d

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True

                    if d <= safety[nx][ny]:
                        q.appendleft((d, nx, ny))
                    else:
                        q.append((safety[nx][ny], nx, ny))

        return 0
