#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(num1, num2):
            int1, int2 = int(num1 + num2), int(num2 + num1)
            if int1 > int2:
                return 1
            elif int1 < int2:
                return -1
            else:
                return 0

        nums = [str(num) for num in nums]
        nums = sorted(nums, key=cmp_to_key(comparator), reverse=True)
        return '0' if nums[0] == '0' else "".join(nums)

if __name__ == '__main__':
    assert Solution().largestNumber([10, 2]) == "210"
    assert Solution().largestNumber([0, 0]) == "0"