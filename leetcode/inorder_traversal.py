#!/usr/bin/python3
# -*-coding:utf-8-*-

from sum_root_to_leaf_numbers import TreeNode
from create_binary_tree import create_binary_tree

__author__ = "Bannings"


# 中序遍历，"左根右"
def inorder(root: TreeNode):
    nodes = []
    pointer = root
    while pointer or nodes:
        if pointer:
            nodes.append(pointer)
            pointer = pointer.left
        else:
            pointer = nodes.pop()
            print(pointer.val)
            pointer = pointer.right


if __name__ == '__main__':
    root = create_binary_tree([3,2,9,None,None,10,None,None,8,None,4])
    inorder(root)
