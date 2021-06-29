#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        ans = [0] + [float('inf')] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                ans[i] = min(ans[i], ans[i - coin] + 1)

        return ans[-1] if ans[-1] != float('inf') else -1

if __name__ == '__main__':
    assert Solution().coinChange([5,2,1],11) == 3
    assert Solution().coinChange([2],3) == -1
    assert Solution().coinChange([1],0) == 0
    assert Solution().coinChange([1],1) == 1
    assert Solution().coinChange([1],2) == 2
