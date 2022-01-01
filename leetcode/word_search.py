#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(word)
        m = len(board)
        n = len(board[0])

        def find(i, j, index):
            if board[i][j] == word[index]:
                if index == l - 1: return True
                board[i][j] = "#"
                if (i != 0 and find(i-1, j, index+1)) or (i != m-1 and find(i+1, j, index+1)) or (j != 0 and find(i, j-1, index+1)) or (j != n-1 and find(i, j+1, index+1)):
                    return True
                board[i][j] = word[index]
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and find(i, j, 0): return True
        return False

if __name__ == '__main__':
    assert Solution().exist([["a"]], "a")
    assert Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED')
    assert Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'SEE')
    assert not Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB')