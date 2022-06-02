#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[-1])
        ans = [[matrix[j][i] for j in range(m)] for i in range(n)]
        return ans

if __name__ == '__main__':
    assert Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]) == [[1,4,7],[2,5,8],[3,6,9]]
    assert Solution().transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]