#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

import math
from typing import List

class Solution:

    # 方法一
    # def search(self, nums: List[int], target: int) -> int:
    #     length = len(nums)
    #     if length == 0: return -1
    #     low, high = 0, length - 1
    #     while low < high:
    #         pivot_index = (high + low) // 2
    #         if nums[pivot_index] > nums[high]:
    #             low = pivot_index + 1
    #         else:
    #             high = pivot_index
        
    #     pivot_index,low, high = low, 0, length - 1
    #     while low <= high:
    #         mid = (low + high) // 2
    #         adjusted_mid = (mid + pivot_index) % length
    #         if nums[adjusted_mid] == target:
    #             return adjusted_mid
    #         elif nums[adjusted_mid] < target:
    #             low = mid + 1
    #         else:
    #             high = mid - 1
                
    #     return -1

    # 方法二
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        low, high = 0, length - 1
        while low <= high:
            pivot_index = (low + high) // 2
            pivot = nums[pivot_index] \
                if (target < nums[0]) == (nums[pivot_index] < nums[0]) \
                    else (-math.inf if target < nums[0] else math.inf)
                    
            if pivot == target:
                return pivot_index
            elif pivot > target:
                high = pivot_index - 1
            else:
                low = pivot_index + 1

        return -1

if __name__ == '__main__':
    print(Solution().search([1,3], 3))