#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        min_price, max_profit = prices[0], 0
        for price in prices:
            if price <= min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        
        return max_profit

if __name__ == '__main__':
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5
    assert Solution().maxProfit([-1,5,1,5,5]) == 6
    assert Solution().maxProfit([1,5,1,5,5]) == 4
    assert Solution().maxProfit([7,6,4,3,1]) == 0
    assert Solution().maxProfit([]) == 0