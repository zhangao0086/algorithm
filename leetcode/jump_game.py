#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_right = 0
        for i in range(len(nums)):
            if i > max_right: return False
            max_right = max(nums[i] + i, max_right)
        return True

if __name__ == '__main__':
    assert Solution().canJump([]) == True
    assert Solution().canJump([0,3,1,1,4]) == False
    assert Solution().canJump([2,3,1,1,4]) == True
    assert Solution().canJump([3,2,1,0,4]) == False