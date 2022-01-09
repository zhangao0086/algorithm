#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for i in range(n):
            ans[i] = ans[i + n] = nums[i]
        return ans

if __name__ == '__main__':
    assert Solution().getConcatenation([1,2,1]) == [1,2,1,1,2,1]
    assert Solution().getConcatenation([1,3,2,1]) == [1,3,2,1,1,3,2,1]