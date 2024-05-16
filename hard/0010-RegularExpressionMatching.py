"""
Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/
"""


# baab   a.*b


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)  # have we reached the end?
                else:
                    first_match = i < len(s) and p[j] in (s[i], ".")
                    if j + 1 < len(p) and p[j + 1] == "*":
                        ans = (
                            dp(i, j + 2) or first_match and dp(i + 1, j)
                        )  # 0 occurences or 1+ occurences
                    else:
                        ans = first_match and dp(
                            i + 1, j + 1
                        )  # if there is no * move to the next letter
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
