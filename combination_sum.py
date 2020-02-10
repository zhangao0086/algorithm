#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[[]]] + [[] for length in range(target)]
        for candidate in candidates:
            for index in range(candidate, target + 1):
                position = index - candidate
                dp[index] += [combination + [candidate] for combination in dp[position]]
        return dp[target]

if __name__ == '__main__':
    print(Solution().combinationSum([2,3,6,7], 7))