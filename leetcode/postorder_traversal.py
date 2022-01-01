#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from sum_root_to_leaf_numbers import TreeNode
from create_binary_tree import create_binary_tree


# 后序遍历，"左右根"
def postorder(root: TreeNode):
    nodes = [root]
    pre = None

    while nodes:
        pointer = nodes[-1]

        if pointer.left is None and pointer.right is None or (pre is not None and (pointer.left == pre or pointer.right == pre)):
            print(pointer.val)
            pre = pointer
            nodes.pop()
        else:
            if pointer.right:
                nodes.append(pointer.right)

            if pointer.left:
                nodes.append(pointer.left)


if __name__ == '__main__':
    root = create_binary_tree([3,2,9,None,None,10,None,3,None,None,8,None,4])
    postorder(root)
