"""
1339. Maximum Product of Splitted Binary Tree
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = ans = 0

        def sumtree(node):
            nonlocal ans
            if node:
                l = sumtree(node.left)
                r = sumtree(node.right)
                if total:  # if already known (second call)
                    ans = max(ans, l * (total - l), r * (total - r))
                return l + node.val + r
            return 0

        total = sumtree(root)  # find total sum
        sumtree(root)  # check all possible products
        return int(ans % (1e9 + 7))
