from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the list
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        dummy_head = ListNode(-1)
        temp_prev, curr = dummy_head, prev

        while curr:
            if curr.val >= temp_prev.val:
                temp_prev.next = curr
                temp_prev = curr
                curr = curr.next
            else:
                curr = curr.next
        temp_prev.next = None

        new_prev = None
        curr = dummy_head.next
        while curr:
            curr.next, new_prev, curr = new_prev, curr, curr.next

        return new_prev
