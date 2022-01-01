#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        current = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                current[j] += current[j-1]
        return current[-1]

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         previous, current = [1] * n, [1] * n
#         for _ in range(1, m):
#             for j in range(1, n):
#                 current[j] = previous[j] + current[j-1]
#             previous, current = current, previous
#         return previous[-1]

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[1] * n for i in range(m)]
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
#         return dp[m-1][n-1]
    
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         self.cache = [[-1] * n for i in range(m)]
#         return self.dp(m, n)
    
#     def dp(self, m: int, n: int) -> int:
#         if m == 0 or n == 0: return 0
#         if m == 1 and n == 1: return 1

#         if self.cache[m-1][n-1] != -1:
#             return self.cache[m-1][n-1]
        
#         count = self.dp(m - 1, n) + self.dp(m, n - 1)
#         self.cache[m-1][n-1] = count
#         return count

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         if m == 0 or n == 0: return 0
#         if m == 1 and n == 1: return 1
#         return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

if __name__ == '__main__':
    print(Solution().uniquePaths(23, 12))
    print(Solution().uniquePaths(3, 2))
    print(Solution().uniquePaths(7, 3))