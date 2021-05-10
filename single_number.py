#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

# XOR
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         ans = 0
#         for num in nums:
#             ans ^= num
#         return ans

# MATH
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

if __name__ == '__main__':
    assert Solution().singleNumber([2,2,1]) == 1
    assert Solution().singleNumber([4,1,2,1,2]) == 4
    assert Solution().singleNumber([1]) == 1