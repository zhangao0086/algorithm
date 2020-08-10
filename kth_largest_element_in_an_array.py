#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:

    # 方法一：基于快排的划分
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     start, end = 0, len(nums) - 1
    #     target = len(nums) - k
    #     while True:
    #         pivot_index = self.partition(nums, start, end)
    #         if pivot_index == target:
    #             return nums[pivot_index]
    #         elif pivot_index < target:
    #             start = pivot_index + 1
    #         else:
    #             end = pivot_index - 1
    #     return -1

    # def partition(self, nums: List[int], start: int, end: int) -> int:
    #     pivot = nums[start]
    #     pivot_index = start
    #     for i in range(start+1, end+1):
    #         if nums[i] < pivot:
    #             pivot_index += 1
    #             nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
        
    #     nums[pivot_index], nums[start] = nums[start], nums[pivot_index]
    #     return pivot_index

    # 方法二：基于堆排序
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def down_adjust(index: int, length: int):
            temp = nums[index]
            child_index = index * 2 + 1
            while child_index < length:
                if child_index + 1 < length and nums[child_index + 1] > nums[child_index]:
                    child_index += 1
                
                if temp > nums[child_index]:
                    break
                
                nums[child_index], nums[index] = nums[index], nums[child_index]
                index = child_index
                child_index = index * 2 + 1

        def heapify(max_len: int) -> List[int]:
            for index in range((max_len - 2) // 2, -1, -1):
                down_adjust(index, max_len)
            return nums

        heap = heapify(len(nums))
        for i in range(k-1):
            max_len = len(nums)-i-1
            nums[0] = nums[max_len]
            down_adjust(0, max_len)

        return nums[0]

if __name__ == '__main__':
    assert Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 1) == 6
    assert Solution().findKthLargest([3,2,1,5,6,4], 2) == 5
    assert Solution().findKthLargest([3,2,1,5,6,4], 5) == 2
    assert Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
