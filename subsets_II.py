#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                start = len(result)
            for j in range(len(result) - start, len(result)):
                result.append(result[j] + [nums[i]])
        return result

if __name__ == '__main__':
    print(Solution().subsetsWithDup([]))
    print(Solution().subsetsWithDup([1]))
    print(Solution().subsetsWithDup([1,2,3,2]))