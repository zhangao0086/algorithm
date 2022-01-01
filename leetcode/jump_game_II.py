#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         end = len(nums) - 1
#         if end < 0: return 0

#         note = dict()
#         def min_jumps_number(start: int) -> int:
#             if start == end: return 0
#             if nums[start] >= end - start: return 1

#             if start in note: return note[start]
#             result = float("inf")
#             for i in range(nums[start] -1, -1, -1):
#                 result = min(result, min_jumps_number(start + i + 1))
#                 if result == 1: break
#             result += 1
#             note[start] = result
#             return result
#         return min_jumps_number(0)

# 贪心
class Solution:
    def jump(self, nums: List[int]) -> int:
        current, max_right, jumps = 0, 0, 0
        for i in range(len(nums) - 1):
            max_right = max(max_right, i + nums[i])
            if i == current:
                jumps += 1
                current = max_right
        return jumps

if __name__ == '__main__':
    assert Solution().jump([5,4,3,2,1,0]) == 1
    assert Solution().jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]) == 5
    assert Solution().jump([2,3,0,1,4]) == 2
    assert Solution().jump([2,3,1,1,4]) == 2
    Solution().jump([])
    Solution().jump([1])
    Solution().jump([2])
    Solution().jump([5,1])
    Solution().jump([5,0,1])