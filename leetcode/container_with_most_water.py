#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        water = 0

        while left < right:
            minimum = min(height[left], height[right])
            water = max(minimum * (right - left), water)
            while height[left] <= minimum and left < right:
                left += 1
            while height[right] <= minimum and left < right:
                right -= 1
                
        return water

if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))