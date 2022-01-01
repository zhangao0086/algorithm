#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0: return [[]]
        ans = []
        for i in range(k, n + 1):
            ans += [[i] + item for item in self.combine(i - 1, k - 1)]
        return ans

if __name__ == '__main__':
    print(Solution().combine(4, 3))
    print(Solution().combine(4, 2))
    print(Solution().combine(1, 1))