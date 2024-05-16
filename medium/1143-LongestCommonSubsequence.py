"""
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # create dp table
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                # update dp table
                # if char(text1) == char(text2): 1 + up_left square
                # else: max left and up from current square
                dp[i + 1][j + 1] = (
                    1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])
                )
        return dp[-1][-1]
