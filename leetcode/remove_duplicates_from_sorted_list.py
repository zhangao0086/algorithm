#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            if current.val != current.next.val:
                current = current.next
            else:
                current.next = current.next.next
        return head

if __name__ == '__main__':
    root = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    Solution().deleteDuplicates(root)