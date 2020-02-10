#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 1: return
        
        def reverse(start: int, end: int):
            """
            反转指定的区间
            """
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        index = None
        for i in range(length-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break

        # 降序时，反转成升序
        if index is None:
            reverse(0, length - 1)
            return

        smallest = index + 1
        for i in range(smallest+1, length):
            if nums[i] < nums[index]:
                break
            else:
                smallest = i                
        
        nums[index], nums[smallest] = nums[smallest], nums[index]
        reverse(index + 1, length - 1)

if __name__ == '__main__':
    arr = [2,3,1]
    Solution().nextPermutation(arr)
    print(arr)