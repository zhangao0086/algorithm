#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        # local_count = 0
        # for i in range(1, len(A)):
        #     if A[i] > A[i - 1]:
        #         local_count += 1

        # print(local_count)
        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True

if __name__ == '__main__':
    print(Solution().isIdealPermutation([1,0,2]))