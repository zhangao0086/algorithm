#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = pre_left = pre_right = ListNode(next=head)
        left = right = head
        for _ in range(k-1):
            pre_left = left
            left = left.next
        
        checker = left
        while checker.next:
            pre_right = right
            right = right.next
            checker = checker.next
        
        if left == right: return head
        pre_left.next, pre_right.next = right, left
        left.next, right.next = right.next, left.next

        return dummy.next

if __name__ == '__main__':
    head = ListNode(1, ListNode(2))
    Solution().swapNodes(head, 1)

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # Solution().swapNodes(head, 2)

    head = ListNode(7, ListNode(9, ListNode(6, ListNode(6, ListNode(7, ListNode(8, ListNode(3, ListNode(0, ListNode(9, ListNode(5))))))))))
    Solution().swapNodes(head, 5)
