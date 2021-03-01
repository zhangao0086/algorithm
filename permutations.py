#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, [], ans)
        return ans

    def dfs(self, nums, path, result):
        if not nums:
            result.append(path)
        for index, num in enumerate(nums):
            self.dfs(nums[:index] + nums[index+1:], path + [num], result)

if __name__ == '__main__':
    print(Solution().permute([1,2,3]))
    print(Solution().permute([0,1]))
    print(Solution().permute([1]))