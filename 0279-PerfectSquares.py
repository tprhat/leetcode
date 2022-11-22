"""
279. Perfect Squares
https://leetcode.com/problems/perfect-squares/description/
"""

import math


class Solution:
    def numSquares(self, n: int) -> int:

        # k = 1
        def isPerfectSquare(N):
            floorSqrt = math.floor(math.sqrt(N))
            return N == floorSqrt * floorSqrt

        if isPerfectSquare(n):
            return 1

        # k = 2
        for i in range(n):
            if i ** 2 > n:
                break
            if isPerfectSquare(n - i ** 2):
                return 2

        # k = 3
        def legendreTheorem(N):
            while N % 4 == 0:
                N //= 4

            return N % 8 != 7

        if legendreTheorem(n):
            return 3

        # k = 4, Lagrange's four-square theorem
        return 4
