#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack, i = [], 0
        while i < len(traversal):
            level, value = 0, ""
            while i < len(traversal) and traversal[i] == '-':
                level += 1
                i += 1
            while i < len(traversal) and traversal[i] != '-':
                value += traversal[i]
                i += 1
            while level < len(stack):
                stack.pop()
            
            node = TreeNode(value)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

if __name__ == '__main__':
    ans = Solution().recoverFromPreorder("1-2--3--4-5--6--7")
    ans = Solution().recoverFromPreorder("1-2--3---4-5--6---7")
    ans = Solution().recoverFromPreorder("1-401--349---90--88")
    print(ans)