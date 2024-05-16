"""
938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        val = 0
        if low <= root.val <= high:
            val = root.val
        return (
            val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )
