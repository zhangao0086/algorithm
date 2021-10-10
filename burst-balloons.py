#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List
from functools import cache

# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         nums = [1] + [num for num in nums] + [1]
#         n = len(nums)
#         dp = [[0] * n for _ in range(n)]

#         for i in range(2, n):
#             for left in range(0, n - i):
#                 right = left + i
#                 for j in range(left + 1, right):
#                     dp[left][right] = max(
#                         dp[left][right],
#                         nums[left] * nums[j] * nums[right] + dp[left][j] + dp[j][right]
#                     )
#         return dp[0][-1]

class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]

        @cache
        def dp(left, right) -> int:
            if right - left < 0: return 0
            ans = 0

            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                remaining = dp(left, i - 1) + dp(i + 1, right)
                ans = max(ans, remaining + coins)
            return ans

        return dp(1, len(nums) - 2)

if __name__ == '__main__':
    assert Solution().maxCoins([5, 6]) == 36