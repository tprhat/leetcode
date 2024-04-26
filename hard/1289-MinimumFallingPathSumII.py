from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        INF = 10**5
        # keep track of the best and second best value and the index for each row
        best_min = (INF, None)
        best_min2 = (INF, None)

        for j in range(len(grid)):
            # if new best, shift previous best to second best
            if grid[0][j] < best_min[0]:
                best_min2 = best_min
                best_min = (grid[0][j], j)
            # if new second best, update second best
            elif grid[0][j] < best_min2[0]:
                best_min2 = (grid[0][j], j)

        for i in range(1, len(grid)):
            curr_min = (INF, None)
            curr_min2 = (INF, None)

            for j in range(len(grid)):
                # if j in same column as best, add to second best
                if j == best_min[1]:
                    curr_value = best_min2[0]
                else:
                    curr_value = best_min[0]
                curr_value += grid[i][j]

                if curr_value < curr_min[0]:
                    curr_min2 = curr_min
                    curr_min = (curr_value, j)
                elif curr_value < curr_min2[0]:
                    curr_min2 = (curr_value, j)
            # update best and second best for next row
            best_min = curr_min
            best_min2 = curr_min2

        return best_min[0]
