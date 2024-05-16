"""
223. Rectangle Area
https://leetcode.com/problems/rectangle-area/
"""


class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        r1 = abs(ax1 - ax2) * abs(ay1 - ay2)
        r2 = abs(bx1 - bx2) * abs(by1 - by2)
        x1, x2 = max(ax1, bx1), min(ax2, bx2)
        y1, y2 = max(ay1, by1), min(ay2, by2)
        if x1 >= x2 or y1 >= y2:
            r12 = 0
        else:
            r12 = (x2 - x1) * (y2 - y1)
        return r1 + r2 - r12


print(
    Solution.computeArea(
        Solution(), ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-1, by1=4, bx2=1, by2=6
    )
)
