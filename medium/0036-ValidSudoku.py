"""
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check cols
        for i in zip(*board):
            l = [x for x in i if x != "."]
            if len(l) != len(set(l)):
                return False
        # check rows
        for i in board[:]:
            l = [x for x in i if x != "."]
            if len(l) != len(set(l)):
                return False
        # check boxes
        squares = (
            (0, 0),
            (0, 3),
            (0, 6),
            (3, 0),
            (3, 3),
            (3, 6),
            (6, 0),
            (6, 3),
            (6, 6),
        )

        for x, y in squares:
            box = []
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if board[i][j] != ".":
                        box.append(board[i][j])
            if len(box) != len(set(box)):
                return False

        return True
