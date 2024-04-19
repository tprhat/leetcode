"""
79. Word Search
https://leetcode.com/problems/word-search/
"""
import collections
from itertools import product, chain
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        if len(word) > rows * cols:
            return False

        # there are not enough letters on the board
        if not (cnt := collections.Counter(word)) <= collections.Counter(chain(*board)):
            return False

        # inverse word if freq of first leter is bigger than freq of last letter
        if cnt[word[0]] > cnt[word[-1]]:
            word = word[::-1]

        # dfs
        def dfs(cur_row, cur_col, i):

            if i == len(word):
                return True

            if 0 <= cur_row < rows and 0 <= cur_col < cols and board[cur_row][cur_col] == word[i]:
                board[cur_row][cur_col] = '#'
                moves = [(cur_row, cur_col + 1), (cur_row, cur_col - 1),
                         (cur_row + 1, cur_col), (cur_row - 1, cur_col)]
                dp = any(dfs(row, col, i + 1) for row, col in moves)
                board[cur_row][cur_col] = word[i]
                return dp
            return False

        return any(dfs(i, j, 0) for i, j in product(range(rows), range(cols)))


print(Solution.exist(Solution(), board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))
