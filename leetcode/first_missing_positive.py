#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, max_num = 0, len(nums)
        while i < max_num:
            if 0 < nums[i] <= max_num and nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
                right_place = nums[i]-1
                nums[i], nums[right_place] = nums[right_place], nums[i]
            else:
                i += 1
        
        for i in range(max_num):
            if nums[i] != i+1:
                return i+1
        return max_num+1

if __name__ == '__main__':
    print(Solution().firstMissingPositive([-1,4,2,1,9,10]))
    print(Solution().firstMissingPositive([]))
    print(Solution().firstMissingPositive([3,2,1]))
    print(Solution().firstMissingPositive([1,1,2,3,4]))
    print(Solution().firstMissingPositive([1,2,0]))
    print(Solution().firstMissingPositive([3,4,-1,1]))
    print(Solution().firstMissingPositive([7,8,9,11,12]))
    print(Solution().firstMissingPositive([0,-1]))
    print(Solution().firstMissingPositive([-1,-2,-3]))
    print(Solution().firstMissingPositive([3,3]))
    print(Solution().firstMissingPositive([-1]))