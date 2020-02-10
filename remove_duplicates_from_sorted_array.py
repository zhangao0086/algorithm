#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[length] = nums[i]
                length += 1
        return length

if __name__ == '__main__':
    print(Solution().removeDuplicates([1,1,2]))
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))