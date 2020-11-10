#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         j, n = 0, len(nums)
#         for i in range(n):
#             if nums[i] == 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 j += 1
#         for i in range(j,n):
#             if nums[i] == 1:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 j += 1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, low, high = 0, 0, len(nums)-1
        while i <= high:
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                i +=1; low += 1
            elif nums[i] == 2:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
            else:
                i += 1

if __name__ == '__main__':
    nums = [1,2,0]
    Solution().sortColors(nums)
    print(nums)

    nums = [2,0,2,1,1,0]
    Solution().sortColors(nums)
    print(nums)

    nums = [2,0,1]
    Solution().sortColors(nums)
    print(nums)

    nums = [0]
    Solution().sortColors(nums)
    print(nums)

    nums = [1]
    Solution().sortColors(nums)
    print(nums)