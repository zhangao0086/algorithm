#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        table = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.': continue

                row_key = f'{i}_{board[i][j]}'
                column_key = f'{j}-{board[i][j]}'
                grid_key = f'{(i // 3) * 3 + (j // 3)}:{board[i][j]}'
                if row_key in table or column_key in table or grid_key in table:
                    return False

                table.add(row_key)
                table.add(column_key)
                table.add(grid_key)
        return True

if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    assert Solution().isValidSudoku(board)

    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    assert Solution().isValidSudoku(board) == False