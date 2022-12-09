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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        self.traverse(root, root.val, root.val, ans)
        return ans[0]
    
    def traverse(self, root, low, high, ans):
        if not root: return 0
        ans[0] = max(ans[0], abs(root.val-low), abs(root.val-high))
        self.traverse(root.left, min(low, root.val), max(high, root.val), ans)
        self.traverse(root.right, min(low, root.val), max(high, root.val), ans)

if __name__ == '__main__':
    root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))
    assert Solution().maxAncestorDiff(root) == 7