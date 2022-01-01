#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if not head: return head
        
#         fake = ListNode(next=head)
#         fast, slow = head.next, fake
#         while fast:
#             slow.next.next, slow.next, fast.next = fast.next, fast, slow.next
#             slow = slow.next.next
#             fast = fast.next.next
#             if fast: fast = fast.next

#         return fake.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        fake = ListNode(next=head)
        temp = fake
        while temp.next and temp.next.next:
            next = temp.next.next.next
            temp.next, temp.next.next, temp.next.next.next = temp.next.next, temp.next, next
            temp = temp.next.next

        return fake.next

def print_list(root: ListNode):
    ans, node = [], root
    while node:
        ans.append(node.val)
        node = node.next
    print(ans)

if __name__ == '__main__':
    print_list(Solution().swapPairs(ListNode(1)))

    root = ListNode(1, ListNode(2))
    print_list(Solution().swapPairs(root))

    root = ListNode(1, ListNode(2, ListNode(3)))
    print_list(Solution().swapPairs(root))

    root = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print_list(Solution().swapPairs(root))

    root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print_list(Solution().swapPairs(root))

    print_list(Solution().swapPairs(None))