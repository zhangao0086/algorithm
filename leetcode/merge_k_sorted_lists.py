#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        tail = dummy
        while lists:
            min_index = 0
            for i in range(1, len(lists)):
                if lists[i] and (not lists[min_index] or lists[i].val < lists[min_index].val):
                    min_index = i
            if lists[min_index] == None: break
            else:
                tail.next = lists[min_index]
                tail = tail.next
                lists[min_index] = tail.next
                if not tail.next: del lists[min_index]
        return dummy.next

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         if not lists: return None
#         half = len(lists) // 2
#         if half:
#             left, right = self.mergeKLists(lists[:half]), self.mergeKLists(lists[half:])
#             dummy = tail = ListNode(0)
#             while left and right:
#                 if left.val < right.val:
#                     tail.next = left
#                     left = left.next
#                 else:
#                     tail.next = right
#                     right = right.next
#                 tail = tail.next
#             tail.next = left or right
#             return dummy.next
#         else:
#             return lists[0]

if __name__ == '__main__':
    ans = Solution().mergeKLists([
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6))
    ])
    print(ans)