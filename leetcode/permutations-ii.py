#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            perms = [p[:i] + [num] + p[i:] for p in perms for i in range((p + [num]).index(num) + 1)]
        return perms

if __name__ == '__main__':
    print(Solution().permuteUnique([1,1,2]))
    print(Solution().permuteUnique([1,2,3]))