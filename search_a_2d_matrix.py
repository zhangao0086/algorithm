#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n
        
        while low < high:
            mid = low + (high - low) // 2
            value = matrix[mid//n][mid%n]
            if value == target:
                return True
            elif value < target:
                low = mid + 1
            else:
                high = mid
        return False

if __name__ == '__main__':
    assert Solution().searchMatrix([[1]], 0) == False
    assert Solution().searchMatrix([[1]], 1) == True
    assert Solution().searchMatrix([[1]], 2) == False
    assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
    assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 2) == False
    assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60) == True
    assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 50) == False
    assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 34) == True
    assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 31) == False