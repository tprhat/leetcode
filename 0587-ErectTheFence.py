"""
587. Erect the Fence
https://leetcode.com/problems/erect-the-fence/
"""
from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> set[tuple]:

        # https://www.youtube.com/watch?v=eu6i7WJeinw
        def CrossProduct(p1, p2, p3):
            a = p2[0] - p1[0]
            b = p2[1] - p1[1]
            c = p3[0] - p1[0]
            d = p3[1] - p1[1]
            return a * d - b * c

        def convexHalfHull(points):
            stack = []
            for p in points:
                # if the cross product of V1 and V2 is positive, this chain is not moving counterclockwise (pop P2
                # from the stack). And if the cross product is negtive, this chain is moving counterclockwise (append
                # P3 to the stack).
                while len(stack) >= 2 and CrossProduct(stack[-2], stack[-1], p) > 0:
                    stack.pop()
                stack.append(tuple(p))
            return stack

        trees.sort()
        leftToRight = convexHalfHull(trees)
        rightToLeft = convexHalfHull(trees[::-1])

        return set(leftToRight + rightToLeft)
