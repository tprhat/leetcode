"""
Delete the Middle Node of a Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# slow points at the head while fast points at the second succesor of head
# fast will come to the end, while slow will be 1 behind the node we wish to delete
# Robert W. Floyd's tortoise and hare algorithm (cycle detection)
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        slow, fast = head, head.next.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next

        return head
