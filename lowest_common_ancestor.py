#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from sum_root_to_leaf_numbers import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return None
        if root == p or root == q: return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        elif right is None:
            return left
        elif left and right:
            return root
        return None

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(7)
    root.left.right.left = TreeNode(10)
    # root.right.left = TreeNode(8)
    root.right.right = TreeNode(9)

    ancestor = Solution().lowestCommonAncestor(root, root.left, root.right.right)
    print(ancestor)
