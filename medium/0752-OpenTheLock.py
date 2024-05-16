import collections
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        visited = set(deadends)
        q = collections.deque()
        # keep track of lock postion and steps
        q.append(["0000", 0])
        # BFS
        while q:
            curr, step = q.popleft()
            if curr == target:
                return step
            # chenge each digit by -1 and +1
            for i in range(4):
                for d in [-1, 1]:
                    new = curr[:i] + str((int(curr[i]) + d) % 10) + curr[i + 1 :]

                    if new not in visited:
                        visited.add(new)
                        q.append([new, step + 1])

        return -1


# print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
print(
    Solution().openLock(
        ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"
    )
)
