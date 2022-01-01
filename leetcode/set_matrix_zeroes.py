#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0: is_col = True
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(1, len(matrix[0])):
                matrix[0][j] = 0
        
        if is_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0

if __name__ == '__main__':
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Solution().setZeroes(matrix)
    assert matrix == [[1,0,1],[0,0,0],[1,0,1]]

    matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
    Solution().setZeroes(matrix)
    assert matrix == [[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]