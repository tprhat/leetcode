"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        open_par = '([{'
        close_par = ')]}'
        stack = []
        for i in s:
            if stack:
                if i in close_par:
                    for j in range(3):
                        if i == close_par[j]:
                            if stack[-1] == open_par[j]:
                                stack.pop()
                            else:
                                return False
                else:
                    stack.append(i)
            elif i in close_par:
                return False
            else:
                stack.append(i)
        if stack:
            return False
        return True
