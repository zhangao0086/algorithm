#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        empty = 1
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j
                elif grid[i][j] == 0:
                    empty += 1

        def dfs(x, y, empty):
            if not(0 <= x < m and 0 <= y < n and grid[x][y] != -1):
                return
            
            if grid[x][y] == 2:
                if empty == 0:
                    self.ans += 1
                return
            
            grid[x][y] = -1
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            grid[x][y] = 0

        dfs(x, y, empty)
        return self.ans

if __name__ == '__main__':
    assert Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]) == 2
    assert Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]) == 4
    assert Solution().uniquePathsIII([[0,1],[2,0]]) == 0