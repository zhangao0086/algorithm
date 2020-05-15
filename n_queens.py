#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:

    # # 原始
    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     if n == 0: return [[]]
    #     matrix = [["."] * n for _ in range(n)]
    #     ans = []

    #     def can_be_here(i, j) -> bool:
    #         for row in range(i):
    #             if matrix[row][j] == 'Q': return False
    #             if j-i+row >= 0 and matrix[row][j-i+row] == 'Q': return False
    #             if j+i-row < n and matrix[row][j+i-row] == 'Q': return False

    #         return True

    #     def dfs(i, j):
    #         if can_be_here(i, j):
    #             matrix[i][j] = 'Q'

    #             if i == n - 1:
    #                 ans.append(["".join(row) for row in matrix])
    #             else:
    #                 for k in range(n):
    #                     dfs(i + 1, k)
    #             matrix[i][j] = '.'

    #     for j in range(n):
    #         dfs(0, j)

    #     return ans

    # # 基于空间的优化
    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     if n == 0: return [[]]
    #     matrix, diagonal_left, diagonal_right = [-1] * n, set(), set()
    #     ans = []
        
    #     def can_be_here(i, j) -> bool:
    #         if j in matrix or (j - i) in diagonal_left or (j + i) in diagonal_right:
    #             return False
    #         return True

    #     def dfs(i, j):
    #         if can_be_here(i, j):
    #             matrix[i] = j
    #             diagonal_left.add(j-i)
    #             diagonal_right.add(j+i)

    #             if i == n - 1:
    #                 ans.append(['.' * column + 'Q' + '.' * (n-column-1) for column in matrix])
    #             else:
    #                 for k in range(n):
    #                     dfs(i + 1, k)
    #             diagonal_right.remove(j+i)
    #             diagonal_left.remove(j-i)
    #             matrix[i] = -1

    #     for j in range(n):
    #         dfs(0, j)

    #     return ans

    # 代码优化
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0: return [[]]
        ans = []

        def dfs(matrix, diagonal_left, diagonal_right):
            i = len(matrix)
            if i == n:
                ans.append(['.' * column + 'Q' + '.' * (n-column-1) for column in matrix])
                return

            for j in range(n):
                if j not in matrix and (j - i) not in diagonal_left and (j + i) not in diagonal_right:
                    dfs(matrix + [j], diagonal_left + [j-i], diagonal_right + [j+i])

        for j in range(n):
            dfs([j], [j], [j])

        return ans

if __name__ == '__main__':
    ans = Solution().solveNQueens(8)
    print(ans)