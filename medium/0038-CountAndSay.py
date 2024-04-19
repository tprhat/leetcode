"""
38. Count and Say
https://leetcode.com/problems/count-and-say/
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        x = self.countAndSay(n - 1)

        s = ""
        y = x[0]
        cnt = 1
        # count the number of occurances of each sequence with same numbers
        for i in range(1, len(x)):
            if x[i] == y:
                cnt += 1

            else:
                s += str(cnt)
                s += str(y)
                y = x[i]
                cnt = 1
        s += str(cnt)
        s += str(y)
        return s
