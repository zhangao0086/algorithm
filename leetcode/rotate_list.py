#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None

        length, fast = 1, head
        while fast.next:
            length += 1
            fast = fast.next

        fast.next = head

        k = k % length
        if k:
            for _ in range(length - k):
                fast = fast.next
        
        root = fast.next
        fast.next = None
        return root

if __name__ == '__main__':
    root = Solution().rotateRight(ListNode(1, ListNode(2, ListNode(3))), 2000000000)
    root = Solution().rotateRight(None, 0)
    root = Solution().rotateRight(ListNode(0, ListNode(1, ListNode(2))), 1)
    root = Solution().rotateRight(ListNode(0, ListNode(1, ListNode(2))), 2)
    root = Solution().rotateRight(ListNode(0, ListNode(1, ListNode(2))), 3)
    root = Solution().rotateRight(ListNode(0, ListNode(1, ListNode(2))), 4)

    root = Solution().rotateRight(ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))), 1)
    root = Solution().rotateRight(ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))), 2)