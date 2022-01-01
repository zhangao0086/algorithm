#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:

    # 充分利用 python 的特性
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        side = len(matrix)
        for i in range(side // 2):
            for j in range(side - side // 2):
                # matrix[i][j], matrix[j][~i], matrix[~i][j], matrix[i][~j] = \
                # matrix[j][~i], matrix[~i][j], matrix[i][~j], matrix[i][j]

                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]

    # 原始解法 
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     side = len(matrix)
    #     while side > 1:
    #         offset = (len(matrix) - side) // 2
    #         step, i, previous = side - 1, 0, 0
    #         while i < side - 1:
    #             j = i
    #             while j < i + step * 4 + 1:
    #                 if j < side:
    #                     x, y = 0, j
    #                 elif j < side * 2 - 1:
    #                     x, y = j - side + 1, side - 1
    #                 elif j < side * 3 - 2:
    #                     x, y = side - 1, side * 3 - 3 - j
    #                 elif j < side * 4 - 3:
    #                     x, y = side * 4 - 4 - j, 0
    #                 else:
    #                     x, y = 0, i
    #                 previous, matrix[x + offset][y + offset] = matrix[x + offset][y + offset], previous
    #                 j += step
    #             i += 1
    #         side -= 2

if __name__ == '__main__':
    # matrix = [
    #     [1,2],
    #     [3,4],
    # ]
    # Solution().rotate(matrix)
    # print(matrix)

    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    Solution().rotate(matrix)
    print(matrix)

    matrix = [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ]
    Solution().rotate(matrix)
    print(matrix)
