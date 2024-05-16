"""
931. Minimum Falling Path Sum
https://leetcode.com/problems/minimum-falling-path-sum/
"""

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # start from second row and calc min from upper level for each level
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                # up-left
                if i - 1 >= 0 and j - 1 >= 0:
                    p1 = matrix[i - 1][j - 1]
                else:
                    p1 = float("inf")

                # up
                if i - 1 >= 0:
                    p2 = matrix[i - 1][j]
                else:
                    p2 = float("inf")

                # up-right
                if i - 1 >= 0 and j + 1 < len(matrix[0]):
                    p3 = matrix[i - 1][j + 1]
                else:
                    p3 = float("inf")
                # add min value so that current row has min path from top
                matrix[i][j] += min(p1, p2, p3)

        return min(matrix[len(matrix) - 1])
