#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1: return

        index = None
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break

        def reverse(start: int, end: int):
            """
            反转指定的区间
            """
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start+1, end-1

        if index is None:
            """
            当数组完全是降序时，反转成升序
            """
            return reverse(0, n-1)
        
        smallest = index+1
        for i in range(smallest+1, n):
            if nums[i] <= nums[index]:
                break
            else:
                smallest = i

        nums[index], nums[smallest] = nums[smallest], nums[index]
        reverse(index+1, n-1)

if __name__ == '__main__':
    # arr = [2,3,1]
    arr = [1,5,1]
    Solution().nextPermutation(arr)
    print(arr)