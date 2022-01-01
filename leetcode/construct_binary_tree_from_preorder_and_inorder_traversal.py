#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from tree_traversal import TreeNode, levelorder_traversal
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        table = {}
        for index, value in enumerate(inorder):
            table[value] = index
        
        def _recursive(pre_root_index, inorder_left, inorder_right) -> TreeNode:
            if inorder_left > inorder_right: return None
            root = TreeNode(preorder[pre_root_index])
            inorder_index = table[root.value]

            root.left = _recursive(pre_root_index+1, inorder_left, inorder_index-1)
            root.right = _recursive(pre_root_index+inorder_index-inorder_left+1, inorder_index+1, inorder_right)
            return root
        
        return _recursive(0, 0, len(inorder)-1)

if __name__ == '__main__':
    node = Solution().buildTree([1,2,3], [2,3,1])
    print(levelorder_traversal(node))

    node = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
    print(levelorder_traversal(node))