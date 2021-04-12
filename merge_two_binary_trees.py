#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归
# class Solution:
#     def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
#         if not root1: return root2
#         if not root2: return root1

#         root = TreeNode(root1.val + root2.val)
#         root.left = self.mergeTrees(root1.left, root2.left)
#         root.right = self.mergeTrees(root1.right, root2.right)
#         return root

# 迭代
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1: return root2

        stack = [(root1, root2)]
        while stack:
            r1, r2 = stack.pop(0)
            if not r2: continue

            r1.val += r2.val

            if not r1.left:
                r1.left = r2.left
            else:
                stack.append((r1.left, r2.left))
            
            if not r1.right:
                r1.right = r2.right
            else:
                stack.append((r1.right, r2.right))
        return root1

if __name__ == '__main__':
    tree1 = TreeNode(1, TreeNode(3, left=TreeNode(5)), TreeNode(2))
    tree2 = TreeNode(2, TreeNode(1, right=TreeNode(4)), TreeNode(3, right=TreeNode(7)))
    ans = Solution().mergeTrees(tree1, tree2)
    print(ans)