"""
Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l3 = ListNode(0)  # dummyHead, we return l3.next so it does not contain this
        curr = l3
        carry = 0
        while l1 or l2 or carry:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            result = l1val + l2val + carry
            carry = 1 if result >= 10 else 0
            curr.next = ListNode(result % 10)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return l3.next
