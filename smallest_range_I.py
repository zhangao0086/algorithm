#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        # if not A:
        #     return 0

        # minimum, maximum = A[0], A[0]
        # for i in range(1, len(A)):
        #     minimum, maximum = min(minimum, A[i]), max(maximum, A[i])
        
        return max(0, max(A) - min(A) - 2 * K)

if __name__ == '__main__':
    print(Solution().smallestRangeI([2,7,2], 1))
    print(Solution().smallestRangeI([1,4,99,100], 3))