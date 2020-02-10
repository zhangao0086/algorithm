#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.cummulative = []
        sum = 0
        for num in nums:
            sum += num
            self.cummulative.append(sum)
        
    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.cummulative[j]
        else:
            return self.cummulative[j] - self.cummulative[i - 1]

if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sumRange(0,2))
    print(obj.sumRange(2,5))
    print(obj.sumRange(0,5))