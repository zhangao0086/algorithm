#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List
import collections

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:        
        def backtrack(index) -> bool:
            if index == len(empty): return True
            i, j = empty[index]
            for num in rows[i] & columns[j] & boxes[i//3*3+j//3]:
                rows[i].remove(num)
                columns[j].remove(num)
                boxes[i//3*3+j//3].remove(num)
                board[i][j] = str(num)
                if backtrack(index+1): return True
                rows[i].add(num)
                columns[j].add(num)
                boxes[i//3*3+j//3].add(num)
            return False
        
        rows = [set(range(1, 10)) for _ in range(9)]
        columns = [set(range(1, 10)) for _ in range(9)]
        boxes = [set(range(1, 10)) for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i].remove(num)
                    columns[j].remove(num)
                    boxes[i//3*3+j//3].remove(num)
                else:
                    empty.append((i, j))
        backtrack(0)

if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
    Solution().solveSudoku(board)
    print(1)