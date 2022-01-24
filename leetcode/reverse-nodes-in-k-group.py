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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = jump = ListNode()
        dummy.next = right = left = head
        while True:
            count = 0
            while right and count < k:
                right = right.next
                count += 1
            if count == k:
                pre, node = right, left
                for _ in range(k):
                    node.next, node, pre = pre, node.next, node
                jump.next, jump, left = pre, left, right
            else:
                return dummy.next

if __name__ == '__main__':
    head = ListNode(1, ListNode(2))
    node = Solution().reverseKGroup(head, 2)
    print(node)

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    node = Solution().reverseKGroup(head, 2)
    print(node)

    node = Solution().reverseKGroup(head, 3)
    print(node)