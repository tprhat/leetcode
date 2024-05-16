"""
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""

from math import inf
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -inf

        # post order traversal of subtree rooted at `node`
        def walk(node):
            nonlocal max_path
            if node:
                left = walk(node.left)
                right = walk(node.right)

                max_path = max(
                    max_path,
                    node.val + left + right,
                    node.val,
                    node.val + left,
                    node.val + right,
                )
                return max(node.val, node.val + left, node.val + right)
            return 0

        walk(root)
        return int(max_path)
