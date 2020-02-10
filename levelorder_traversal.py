#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from sum_root_to_leaf_numbers import TreeNode
from create_binary_tree import create_binary_tree


# 层序遍历(递归)
def levelorder(root: TreeNode):
    nums = []
    levelorder2(root, 1, nums)
    print(nums)


def levelorder2(root: TreeNode, level, nums: [int]):
    if root:
        if len(nums) == level - 1:
            nums.append([])
        nums[level-1].append(root.val)
        levelorder2(root.left, level + 1, nums)
        levelorder2(root.right, level + 1, nums)


if __name__ == '__main__':
    root = create_binary_tree([3,2,9,None,None,10,3, None,None,None,8,None])
    levelorder(root)
