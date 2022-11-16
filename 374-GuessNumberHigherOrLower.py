"""
374. Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower/description/
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower = 1
        higher = n

        while lower <= higher:
            pick = (lower + higher) // 2
            num = guess(pick)  # guess function is pre-defined
            if num == -1:
                higher = pick - 1
            elif num == 1:
                lower = pick + 1
            else:
                return pick
