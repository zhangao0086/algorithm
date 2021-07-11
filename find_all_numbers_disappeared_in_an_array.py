#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

if __name__ == '__main__':
    assert Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5,6]
    assert Solution().findDisappearedNumbers([1,1]) == [2]