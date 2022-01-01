#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     def _findTargetSumWays(i: int, target: int) -> int:
    #         if i == len(nums):
    #             return int(target == 0)
    #         else:
    #             return _findTargetSumWays(i + 1, target + nums[i]) + _findTargetSumWays(i + 1, target - nums[i])
        
    #     ans = _findTargetSumWays(0, target)
    #     return ans

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = { 0 : 1 }
        for num in nums:
            dp2 = {}
            for old_key in dp.keys():
                new_key_1 = old_key + num
                dp2[new_key_1] = dp2.get(new_key_1, 0) + dp[old_key]

                new_key_2 = old_key - num
                dp2[new_key_2] = dp2.get(new_key_2, 0) + dp[old_key]
            dp = dp2
        return dp.get(target, 0)

if __name__ == '__main__':
    # assert Solution().findTargetSumWays([1,1,1,1,1], 3) == 5
    # assert Solution().findTargetSumWays([1,0], 1) == 2
    assert Solution().findTargetSumWays([0,38,42,31,13,10,11,12,44,16,38,17,22,28,9,27,20,35,34,39], 2) == 6666