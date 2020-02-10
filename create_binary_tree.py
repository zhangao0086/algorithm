#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from sum_root_to_leaf_numbers import TreeNode

def create_binary_tree(list: [int]) -> TreeNode:
    if list is None or len(list) == 0:
        return None

    val = list.pop(0)
    if val is not None:
        node = TreeNode(val)
        node.left = create_binary_tree(list)
        node.right = create_binary_tree(list)
        return node
    else:
        return None


if __name__ == '__main__':
    root = create_binary_tree([3, 2, 9, None, None, 10, None, None, 8, None, 4])
    print(root)
