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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root, 0)
        return root
    
    def dfs(self, root: Optional[TreeNode], base: int) -> Optional[TreeNode]:
        if root is None: return base

        right = self.dfs(root.right, base)
        left = self.dfs(root.left, root.val + right)

        root.val += right
        return left

def build_bst(nums: list, index = 0) -> TreeNode:
    if len(nums) <= index: return None
    if nums[index] is None: return None

    root = TreeNode(nums[index])
    root.left = build_bst(nums, index * 2 + 1)
    root.right = build_bst(nums, index * 2 + 2)
    return root

if __name__ == '__main__':
    root = build_bst([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
    ans = Solution().convertBST(root)
    print(ans)