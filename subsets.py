#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ans = [[]]
#         for num in nums:
#             ans += [subset + [num] for subset in ans]
#         return ans

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def trace(index, curr):
            ans.append(curr)
            for i in range(index, n):
                trace(i + 1, curr + [nums[i]])
        
        trace(0, [])
        return ans

if __name__ == '__main__':
    print(Solution().subsets([1,2,3]))
    print(Solution().subsets([]))
    print(Solution().subsets([1]))
    print(Solution().subsets([1,3,4,5]))