#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(nums[i] + ans[-1])
        return ans

if __name__ == '__main__':
    assert Solution().runningSum([1,2,3,4]) == [1,3,6,10]
    assert Solution().runningSum([1,1,1,1,1]) == [1,2,3,4,5]
    assert Solution().runningSum([3,1,2,10,1]) == [3,4,6,16,17]