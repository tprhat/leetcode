from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        ans = []

        def construct(index, current):
            if index == N:
                ans.append(current[:])
                return

            for end in range(index, N):
                if s[index : end + 1] == s[index : end + 1][::-1]:
                    current.append(s[index : end + 1])
                    construct(end + 1, current)
                    current.pop()

        construct(0, [])
        return ans
