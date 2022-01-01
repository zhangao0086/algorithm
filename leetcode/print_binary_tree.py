#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from sum_root_to_leaf_numbers import TreeNode
from typing import List

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        if root is None:
            return []

        def level_traversal(root: TreeNode) -> (int, int):
            m, stack = 0, [root]
            while stack:
                count = len(stack)
                m += 1
                while count > 0:
                    node = stack.pop(0)

                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                    count -= 1
            return m, (1 << m) - 1
        
        m, n = level_traversal(root)
        matrix = [[""] * n for x in range(m)]

        level, stack = 0, [(root, n, -1)]
        while stack:
            count = len(stack)
            while count > 0:
                node, parent_location, assign  = stack.pop(0)
                node_location = parent_location + (1 << (m - level - 1)) * assign
                matrix[level][node_location] = str(node.val)

                if node.left:
                    stack.append((node.left, node_location, -1))
                if node.right:
                    stack.append((node.right, node_location, 1))

                count -= 1
            level += 1
        return matrix

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(5)
    root.right = TreeNode(8)
    root.left.right = TreeNode(10)

    print(Solution().printTree(root))