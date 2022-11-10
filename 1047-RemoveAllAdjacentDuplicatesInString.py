"""
1047. Remove All Adjacent Duplicates In String
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            else:
                if stack[-1] == s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
        return ''.join(stack)
