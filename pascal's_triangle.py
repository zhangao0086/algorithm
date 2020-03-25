#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        result = [[1]]
        for row in range(1, numRows):
            result.append([1])
            for col in range(1, row):
                result[row].append(result[row-1][col-1] + result[row-1][col])
            
            result[row].append(1)
        return result

if __name__ == '__main__':
    print(Solution().generate(5))