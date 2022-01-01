#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        root = ListNode(0, head)
        fast, slow = root, root
        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return root.next

if __name__ == '__main__':
    root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ans = Solution().removeNthFromEnd(root, 2)
    print(ans)

    root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ans = Solution().removeNthFromEnd(root, 5)
    print(ans)

    root = ListNode(1)
    ans = Solution().removeNthFromEnd(root, 1)
    print(ans)

    root = ListNode(1, ListNode(2))
    ans = Solution().removeNthFromEnd(root, 1)
    print(ans)