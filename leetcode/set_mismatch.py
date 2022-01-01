#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup = -1
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                dup = abs(nums[i])
            else:
                nums[index] *= -1
        
        missing = -1
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
                break

        return [dup, missing]

if __name__ == '__main__':
    print(Solution().findErrorNums([1,2,2,4]))