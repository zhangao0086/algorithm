#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            index = int((high + low) / 2)
            if nums[index] == target:
                return index
            elif nums[index] > target:
                high = index - 1
            else:
                low = index + 1
        return low

if __name__ == '__main__':
    print(Solution().searchInsert([1,3,5,6], 5))
    print(Solution().searchInsert([1,3,5,6], 2))
    print(Solution().searchInsert([1,3,5,6], 7))
    print(Solution().searchInsert([1,3,5,6], 0))
    print(Solution().searchInsert([1,3,5,6], -1))
    print(Solution().searchInsert([], 0))
