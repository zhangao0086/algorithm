#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0: return 0

        def dfs(matrix, diagonal_left, diagonal_right):
            i = len(matrix)
            if i == n: 
                self.ans += 1
                return

            for j in range(n):
                if j not in matrix and (j - i) not in diagonal_left and (j + i) not in diagonal_right:
                    dfs(matrix + [j], diagonal_left + [j-i], diagonal_right + [j+i])

        self.ans = 0
        for j in range(n):
            dfs([j], [j], [j])

        return self.ans

if __name__ == '__main__':
    assert Solution().totalNQueens(4) == 2