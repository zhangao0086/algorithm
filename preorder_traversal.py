#!/usr/bin/python3
# -*-coding:utf-8-*-

from sum_root_to_leaf_numbers import TreeNode
from create_binary_tree import create_binary_tree

__author__ = "Bannings"


# 前序遍历，又称先序遍历，"根左右"
def preorder(root: TreeNode):
    nodes = []
    pointer = root
    while pointer or nodes:
        if pointer:
            print(pointer.val)
            nodes.append(pointer)
            pointer = pointer.left
        else:
            pointer = nodes.pop().right


if __name__ == '__main__':
    root = create_binary_tree([3,2,9,None,1,None,None,10,None,None,8,None,4])
    preorder(root)