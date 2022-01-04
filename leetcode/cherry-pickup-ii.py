#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List
from functools import cache

class Solution:
    """
    Top Down
    """
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @cache
        def dp(row, col1, col2) -> int:
            ans = grid[row][col1]
            if col1 != col2:
                ans += grid[row][col2]
            if row < m-1:
                ans += max(
                    [dp(row+1, new_col1, new_col2) 
                    for new_col1 in range(max(0, col1-1), min(col1+2, n))
                    for new_col2 in range(max(0, col2-1), min(col2+2, n))])
            return ans
        return dp(0, 0, n-1)

class Solution:
    """
    Bottom Up
    """
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[0]*n for _ in range(n)] for __ in range(m)]

        for row in reversed(range(m)):
            for col1 in range(n):
                for col2 in range(n):
                    ans = grid[row][col1]
                    if col1 != col2:
                        ans += grid[row][col2]
                    if row < m-1:
                        ans += max(dp[row+1][new_col1][new_col2]
                                      for new_col1 in [col1, col1+1, col1-1]
                                      for new_col2 in [col2, col2+1, col2-1]
                                      if 0 <= new_col1 < n and 0 <= new_col2 < n)
                    dp[row][col1][col2] = ans

        return dp[0][0][n-1]

if __name__ == '__main__':
    assert Solution().cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]) == 24
    assert Solution().cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]) == 28