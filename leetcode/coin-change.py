#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

# 递归
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def recursive(remainder, cache):
            if remainder < 0: return -1
            if remainder == 0: return 0

            if cache[remainder-1] != 0: return cache[remainder-1]

            min = float("inf")
            for coin in coins:
                res = recursive(remainder - coin, cache)
                if res >= 0 and res < min:
                    min = 1 + res
            
            cache[remainder-1] = -1 if min == float("inf") else min
            return cache[remainder-1]
        
        if amount < 1: return 0
        return recursive(amount, [0] * amount)

# dp
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        ans = [0] + [float('inf')] * amount
        for coin in coins:
            for i in range(coin, amount+1):
                ans[i] = min(ans[i], ans[i-coin]+1)
        
        return ans[-1] if ans[-1] != float('inf') else -1

if __name__ == '__main__':
    assert Solution().coinChange([5,2,1], 11) == 3
    assert Solution().coinChange([2], 3) == -1
    assert Solution().coinChange([1], 0) == 0
    assert Solution().coinChange([1], 1) == 1
    assert Solution().coinChange([1], 2) == 2