#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.val

        cumulator = 0
        nodes = [(root, 0)]
        while len(nodes) > 0:
            node, high = nodes.pop(0)

            carry = high + node.val
            if node.left is None and node.right is None:
                cumulator += carry
                continue

            if node.left is not None:
                nodes.append((node.left, carry * 10))

            if node.right is not None:
                nodes.append((node.right, carry * 10))

        return cumulator

        # while len(nodes) > 0:
        #     node = nodes.pop(0)
        #
        #     if node.left is None and node.right is None:
        #         cumulator += node.val
        #
        #     if node.left is not None:
        #         node.left.val += node.val * 10
        #         nodes.append(node.left)
        #
        #     if node.right is not None:
        #         node.right.val += node.val * 10
        #         nodes.append(node.right)
        #
        # return cumulator

    #     return self.sumNumbers2(root, 0)
    #
    # def sumNumbers2(self, root: TreeNode, cumulator: int) -> int:
    #     if root is None:
    #         return 0
    #
    #     cumulator = cumulator * 10 + root.val
    #     if root.left is None and root.right is None:
    #         return cumulator
    #     else:
    #         return self.sumNumbers2(root.left, cumulator) + self.sumNumbers2(root.right, cumulator)


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(5)
    root.right = TreeNode(5)
    root.left.right = TreeNode(5)
    print(Solution().sumNumbers(root))