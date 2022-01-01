#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return f'{self.val}'

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         stack = [(root, None, None)]
#         while stack:
#             node, min, max = stack.pop()

#             if node.right:
#                 if node.right.val <= node.val: return False
#                 if max and max <= node.right.val: return False
#                 if node.right.left or node.right.right:
#                     stack.append((node.right, node.val, max))

#             if node.left:
#                 if node.left.val >= node.val: return False
#                 if min and min >= node.left.val: return False
#                 if node.left.left or node.left.right:
#                     stack.append((node.left, min, node.val))
                 
#         return True

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, min = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if root.val <= min: return False
            min, root = root.val, root.right

        return True

if __name__ == '__main__':
    root = TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2, right=TreeNode(3))), TreeNode(5, TreeNode(4), TreeNode(6)))
    assert not Solution().isValidBST(root)

    root = TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(6)))
    assert Solution().isValidBST(root)

    root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
    assert not Solution().isValidBST(root)

    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert Solution().isValidBST(root)

    root = TreeNode(5, TreeNode(1), TreeNode(4))
    assert not Solution().isValidBST(root)

    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert not Solution().isValidBST(root)