#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        
        def leftmost(find_target: int, low = 0, high = len(nums) - 1) -> int:
            while low < high:
                pivot_index = (low + high) // 2
                if nums[pivot_index] < find_target:
                    low = pivot_index + 1
                else:
                    high = pivot_index
                    
            return low
        
        low = leftmost(target)
        if nums[low] == target:
            high = leftmost(target + 1, low)
            return [low, high if nums[high] == target else high - 1]
        else:
            return [-1, -1]