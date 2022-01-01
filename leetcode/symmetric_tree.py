#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from sum_root_to_leaf_numbers import TreeNode

def create_binary_tree(list: [int]) -> TreeNode:
    
    def create_node(index: int):
        if index > len(list):
            return None

        root = TreeNode(list[index - 1])
        root.left = create_node(index * 2)
        root.right = create_node(index * 2 + 1)

        return root

    return create_node(1)

class Solution:
    # def isSymmetric(self, root: TreeNode) -> bool:

    #     def is_mirror(tree1, tree2) -> bool:
    #         if tree1 is None and tree2 is None: return True
    #         if tree1 is None or tree2 is None: return False
    #         return tree1.val == tree2.val and is_mirror(tree1.left, tree2.right) and is_mirror(tree1.right, tree2.left)
        
    #     return is_mirror(root, root)

    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [root, root]
        while stack:
            tree1, tree2 = stack.pop(0), stack.pop(0)
            if tree1 is None and tree2 is None: continue
            if tree1 is None or tree2 is None: return False
            if tree1.val != tree2.val: return False

            stack.append(tree1.left)
            stack.append(tree2.right)
            stack.append(tree1.right)
            stack.append(tree2.left)
        return True
        
if __name__ == '__main__':
    assert Solution().isSymmetric(create_binary_tree([1,2,2,3,4,4,3]))
    assert not Solution().isSymmetric(create_binary_tree([1,2,2,None,3,None,3]))