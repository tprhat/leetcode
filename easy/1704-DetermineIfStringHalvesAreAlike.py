"""
1704. Determine if String Halves Are Alike
https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        s = s.lower()
        vovels = 'aeiou'
        cnt_left, cnt_right = 0, 0
        left, right = s[:n // 2], s[n // 2:]
        for i in left:
            if i in vovels:
                cnt_left += 1
        for i in right:
            if i in vovels:
                cnt_right += 1

        return cnt_left == cnt_right
        # oneliner!
        # return sum(c.lower() in 'aeiou' for c in s[: len(s)//2]) == sum(c.lower() in 'aeiou' for c in s[len(s)//2 :])
