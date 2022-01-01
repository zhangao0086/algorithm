#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0: profit += diff
        return profit

if __name__ == '__main__':
    print(Solution().maxProfit([1,2,3,4,5]))
    print(Solution().maxProfit([7,1,5,3,6,4]))
    print(Solution().maxProfit([1,7,2,3,6,7,6,7]))

