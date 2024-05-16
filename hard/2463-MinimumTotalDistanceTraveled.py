"""
2463. Minimum Total Distance Traveled
https://leetcode.com/problems/minimum-total-distance-traveled/description/
"""

from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factories = []
        for i in range(len(factory)):
            factories.extend([factory[i][0]] * factory[i][1])
        n, m = len(robot), len(factories)
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        robot.sort()
        factories.sort()

        def solve(i, j):
            if i == n:
                return 0
            if j == m:
                return 1e13
            if dp[i][j] != -1:
                return dp[i][j]
            ans = 1e13
            # if we form a pair we add the distance to ans
            ans = min(ans, solve(i + 1, j + 1) + abs(robot[i] - factories[j]))
            # if we dont form a pair we remove 1 factory
            ans = min(ans, solve(i, j + 1))
            dp[i][j] = ans
            return ans

        return solve(0, 0)


# cleaner solution
"""
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        @cache
        def dp(i, j, k):
            if i == len(robot): return 0
            if j == len(factory): return inf
            res1 = dp(i, j + 1, 0)
            res2 = dp(i + 1, j, k + 1) + abs(robot[i] - factory[j][0]) if factory[j][1] > k else inf
            return min(res1, res2)
        return dp(0, 0, 0)
"""
