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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        
        targetSum -= root.val
        if not (root.left or root.right):
            return targetSum == 0
        else:
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

if __name__ == '__main__':
    root = TreeNode(-2, right=TreeNode(-3))
    assert Solution().hasPathSum(root, -5)

    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, right=TreeNode(1))))
    assert Solution().hasPathSum(root, 22)

    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert not Solution().hasPathSum(root, 5)

    root = None
    assert not Solution().hasPathSum(root, 0)