#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         if not obstacleGrid: return 0
#         m, n = len(obstacleGrid), len(obstacleGrid[0])
#         current = [1] + [0] * (n - 1)
#         for i in range(m):
#             for j in range(n):
#                 if obstacleGrid[i][j] == 1:
#                     current[j] = 0
#                 elif j > 0:
#                     current[j] += current[j - 1]

#         return current[-1]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        if not obstacleGrid[0]: return 1
        if obstacleGrid[0][0] == 1: return 0

        obstacleGrid[0][0] = 1
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(1, n):
            obstacleGrid[0][i] = int(obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1] == 1)
        
        for j in range(1, m):
            obstacleGrid[j][0] = int(obstacleGrid[j][0] == 0 and obstacleGrid[j-1][0] == 1)
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

        return obstacleGrid[-1][-1]

if __name__ == '__main__':
    # print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    # print(Solution().uniquePathsWithObstacles([[0,0,0]]))
    # print(Solution().uniquePathsWithObstacles([[0,1,0]]))
    # print(Solution().uniquePathsWithObstacles([[0,0]]))
    # print(Solution().uniquePathsWithObstacles([[0]]))
    # print(Solution().uniquePathsWithObstacles([]))
    # print(Solution().uniquePathsWithObstacles([[]]))
    # print(Solution().uniquePathsWithObstacles([[1]]))
    print(Solution().uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))
