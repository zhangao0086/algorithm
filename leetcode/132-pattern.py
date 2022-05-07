#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        stack, maxmid = [], float('-inf')
        for n in nums[::-1]:
            if n < maxmid: return True
            while stack and stack[-1] < n:
                maxmid = stack.pop()
            stack.append(n)

        return False

if __name__ == '__main__':
    assert Solution().find132pattern([1,4,0,-1,-2,-3,-1,-2])