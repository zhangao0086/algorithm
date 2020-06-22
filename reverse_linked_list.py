#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     pre, cur = None, head
    #     while cur:
    #         next = cur.next
    #         cur.next, pre, cur = pre, cur, next

    #     return pre

    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre

if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    res = Solution().reverseList(root)
    print(res)