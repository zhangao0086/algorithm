#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:

    # def getRow(self, rowIndex: int) -> List[int]:
    #     last_row = [1]
    #     for row_index in range(1, rowIndex + 1):
    #         row = []
    #         for col_index in range(1, row_index):
    #             row.append(last_row[col_index - 1] + last_row[col_index])
    #         last_row = [1] + row + [1]

    #     return last_row

    def getRow(self, rowIndex: int) -> List[int]:
        last_row = [1] * (rowIndex + 1)
        for row_index in range(1, rowIndex + 1):
            for col_index in range(1, row_index):
                last_row[row_index - col_index] += last_row[row_index - col_index - 1]

        return last_row

if __name__ == '__main__':
    print(Solution().getRow(0))
    print(Solution().getRow(1))
    print(Solution().getRow(2))
    print(Solution().getRow(3))
    print(Solution().getRow(33))