"""
1926. Nearest Exit from Entrance in Maze
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/
"""
import collections
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        # directions in which we can move
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        start_row, start_col = entrance
        # mark visited cells with '+'
        maze[start_row][start_col] = '+'

        queue = collections.deque()
        queue.append([start_row, start_col, 0])

        # BFS
        while queue:
            cur_row, cur_col, cur_dist = queue.popleft()

            for d in dirs:
                next_row = cur_row + d[0]
                next_col = cur_col + d[1]

                # if next cell is unvisited
                if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == '.':

                    # if it's an exit
                    if next_row == 0 or next_row == rows - 1 or next_col == 0 or next_col == cols - 1:
                        return cur_dist + 1

                    maze[next_row][next_col] = '+'
                    queue.append([next_row, next_col, cur_dist + 1])


        return -1

print(Solution.nearestExit(Solution(), maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]))