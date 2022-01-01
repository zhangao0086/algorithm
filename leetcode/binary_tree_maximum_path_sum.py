#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# Definition for a binary tree node.
from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = float('-inf')
        def _maxPathSum(node: TreeNode) -> int:
            nonlocal ans
            if not node: return 0

            left_sum = max(_maxPathSum(node.left), 0)
            right_sum = max(_maxPathSum(node.right), 0)
            
            val = node.val + left_sum + right_sum
            ans = max(ans, val)
            return node.val + max(left_sum, right_sum)
        _maxPathSum(root)
        return ans

if __name__ == '__main__':
    # root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    # assert Solution().maxPathSum(root) == 42

    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, right=TreeNode(1))))
    assert Solution().maxPathSum(root) == 48
