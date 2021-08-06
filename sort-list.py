#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head

        mid = self.get_mid_node(head)
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)
    
    def merge(self, left: ListNode, right: ListNode):
        dummy = ListNode()
        tail = dummy
        while left and right:
            if left.val < right.val:
                tail.next = left
                tail = left
                left = left.next
            else:
                tail.next = right
                tail = right
                right = right.next
        if left or right:
            tail.next = left if left else right
        return dummy.next
    
    def get_mid_node(self, head: ListNode):
        mid_previous = None
        while head and head.next:
            mid_previous = head if mid_previous is None else mid_previous.next
            head = head.next.next
        mid = mid_previous.next
        mid_previous.next = None
        return mid

if __name__ == '__main__':
    root = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    ans = Solution().sortList(root)
    print(ans)