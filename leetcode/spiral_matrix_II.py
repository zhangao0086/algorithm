#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for i in range(n)]
        
        def get_num(r1, c1, r2, c2):
            for r in range(r1, r2 + 1):
                yield c1, r
            for c in range(c1 + 1, c2 + 1):
                yield c, r2
            for r in range(r2 - 1, r1, -1):
                yield c2, r
            for c in range(c2, c1, -1):
                yield c, r1
        r1, r2 = 0, n - 1
        c1, c2 = 0, n - 1
        i = 1
        while r1 <= r2 and c1 <= c2:
            for c, r in get_num(r1, c1, r2, c2):
                ans[c][r] = i
                i += 1
            r1 += 1; r2 -=1; c1 += 1; c2 -= 1
        return ans

if __name__ == '__main__':
    print(Solution().generateMatrix(3))