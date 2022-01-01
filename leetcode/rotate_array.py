#!/usr/bin/python3
# -*-coding:utf-8-*-
__author__ = "Bannings"

from typing import List
import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        i, count, k = 0, 0, k % len(nums)
        while count < len(nums):
            current = i
            value = nums[i]

            while True:
                next = (current + k) % len(nums)
                value, nums[next], current = nums[next], value, next
                count += 1

                if current == i: break

            i += 1

if __name__ == '__main__':
    nums = [-1,-100,3,99]
    Solution().rotate(nums, 0)
    print(nums)

    nums = [1]
    Solution().rotate(nums, 1)
    print(nums)

    nums = [1,2]
    Solution().rotate(nums, 1)
    print(nums)

    nums = [1,2,3,4,5,6,7]
    Solution().rotate(nums, 3)
    print(nums)

    nums = [1,2]
    Solution().rotate(nums, 0)
    print(nums)

    nums = [1,2,3]
    Solution().rotate(nums, 2)
    print(nums)

    nums = [1,2]
    Solution().rotate(nums, 2)
    print(nums)

    nums = [1,2]
    Solution().rotate(nums, 3)
    print(nums)