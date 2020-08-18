#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:

    # Right-Most 二分查找
    # def countSmaller(self, nums: List[int]) -> List[int]:
    #     arr, ans = [], [0] * len(nums)
            
    #     def right_most(target: int):
    #         left, right = 0, len(arr)
    #         while left < right:
    #             index = (left + right) // 2
    #             if arr[index] >= target:
    #                 right = index
    #             else:
    #                 left = index+1
    #         return left

    #     for i in range(len(nums)-1, -1, -1):
    #         curr = nums[i]
    #         inserted_index = right_most(curr)
    #         if inserted_index == len(arr):
    #             ans[i] = len(arr)
    #             arr.append(curr)
    #         else:
    #             ans[i] = inserted_index
    #             arr.insert(inserted_index, curr)
    #     return ans

    # 归并排序思路
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        def merger_sort(enums: List[int]):
            half = len(enums) // 2
            if half:
                left, right = merger_sort(enums[:half]), merger_sort(enums[half:])
                for index in range(len(enums)-1,-1,-1):
                    if not right or left and left[-1][1] > right[-1][1]:
                        ans[left[-1][0]] += len(right)
                        enums[index] = left.pop()
                    else:
                        enums[index] = right.pop()
            return enums
        merger_sort(list(enumerate(nums)))
        return ans

if __name__ == '__main__':
    print(Solution().countSmaller([5,2,6,1]))