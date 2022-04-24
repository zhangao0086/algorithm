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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur, prev, drops, stack = root, TreeNode(float('-inf')), [], []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if node.val < prev.val: drops.append((prev, node))
            prev, cur = node, node.right
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val

if __name__ == '__main__':
    root = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
    Solution().recoverTree(root)
    print(root)