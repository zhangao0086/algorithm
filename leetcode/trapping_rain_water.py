#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        total, left, right = 0, 0, len(height) - 1
        max_left, max_right = 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    total += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    total += max_right - height[right]
                right -= 1

        return total

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         total, traps, left, right = 0, set(), 0, len(height)-1

#         for index in range(len(height)-1,-1,-1):
#             if height[index] >= height[right]:
#                 if right - index > 1:
#                     traps.add((index, right))
#                 right = index

#         for index in range(len(height)):
#             if height[index] >= height[left]:
#                 if index - left > 1:
#                     traps.add((left, index))
#                 left = index

#         for left, right in traps:
#             total += min(height[left], height[right]) * (right - left - 1)
#             for index in range(left + 1, right):
#                 total -= height[index]

#         return total

if __name__ == '__main__':
    print(Solution().trap([4,2,3]))
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(Solution().trap([0,1,0,2,1,0,1,3,2,3,1,2,1]))
    print(Solution().trap([0]))
    print(Solution().trap([0,0]))
    print(Solution().trap([3,2,3]))
    print(Solution().trap([3,3]))
    print(Solution().trap([]))
    