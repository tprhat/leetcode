"""
1235. Maximum Profit in Job Scheduling
https://leetcode.com/problems/maximum-profit-in-job-scheduling/
"""

from bisect import bisect_left
from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        dp = [[0, 0]]

        def f(x):
            # print(bisect_left(dp, [x + 1]))
            # print(dp[bisect_left(dp, [x + 1]) - 1][1])
            return dp[bisect_left(dp, [x + 1]) - 1][1]

        for end, start, p in sorted(zip(endTime, startTime, profit)):
            dp.append([end, max(f(end), p + f(start))])
            print(dp)
        return dp[-1][1]


#   e     s     p     dp
#  ––-–  ––-–  ––-–  ––––––––––––––––-–
#    3     1    20   [[0,0],[3,20]]
#    5     2    20   [[0,0],[3,20],[5,20]]
#    6     4    70   [[0,0],[3,20],[5,20],[6,90]]
#    9     6    60   [[0,0],[3,20],[5,20],[6,90],[9,150]]
#   10     3   100   [[0,0],[3,20],[5,20],[6,90],[9,150],[10,150]]
#                                                             |
#                                                           answer


print(
    Solution.jobScheduling(
        Solution(),
        startTime=[1, 2, 3, 4, 6],
        endTime=[3, 5, 10, 6, 9],
        profit=[20, 20, 100, 70, 60],
    )
)
