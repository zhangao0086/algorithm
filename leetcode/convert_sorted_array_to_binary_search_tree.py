#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def _sortedArrayToBST(nums: List[int], start, end) -> TreeNode:
            if start < 0 or end < 0 or start > end: return None

            mid = start + (end - start - 1) // 2 + 1
            return TreeNode(nums[mid], _sortedArrayToBST(nums, start, mid-1), _sortedArrayToBST(nums, mid + 1, end))
        return _sortedArrayToBST(nums, 0, len(nums) - 1)

if __name__ == '__main__':
    node = Solution().sortedArrayToBST([-10,-3,0,5,9])
    print(node)