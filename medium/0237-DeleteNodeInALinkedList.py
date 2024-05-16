"""
Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # we update the current node with the value and next of the next node, thus deleting the next node.
        node.val = node.next.val
        node.next = node.next.next
