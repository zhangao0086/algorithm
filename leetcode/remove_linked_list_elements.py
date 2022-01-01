#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        previous = dummy
        while head:
            if head.val != val:
                previous.next = head
                previous = head
            head = head.next
        previous.next = None

        return dummy.next

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(7, ListNode(6)))))
    Solution().removeElements(head, 6)

    head = ListNode(6, ListNode(6, ListNode(6, ListNode(6, ListNode(6)))))
    Solution().removeElements(head, 6)

    head = ListNode(6, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    Solution().removeElements(head, 6)