#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, candidate = 0, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)        
        return candidate

if __name__ == '__main__':
    assert Solution().majorityElement([3,2,3]) == 3
    assert Solution().majorityElement([2,2,1,1,1,2,2]) == 2