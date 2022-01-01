#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from math import sqrt

# 双指针暴力解
class Solution1:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))
        while left <= right:
            num = left*left + right*right
            if num == c:
                return True
            elif num < c:
                left += 1
            else:
                right -= 1
        return False

# 使用 sqrt 的优化版
class Solution2:
    def judgeSquareSum(self, c: int) -> bool:
        for left in range(int(sqrt(c)) + 1):
            right = sqrt((c - left*left))
            if right.is_integer():
                return True
        return False

# 基于二分实现 sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def can_sqrt(num, start, end):
            if start > end: return False
            mid = start + (end - start) // 2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                return can_sqrt(num, mid+1, end)
            else:
                return can_sqrt(num, start, mid-1)

        left = 0
        while left*left <= c:
            right = c - left*left
            if can_sqrt(right, 0, right):
                return True
            left += 1
        return False

if __name__ == '__main__':
    assert Solution().judgeSquareSum(1) == True
    assert Solution().judgeSquareSum(4) == True
    assert Solution().judgeSquareSum(5) == True
    assert Solution().judgeSquareSum(3) == False
    assert Solution().judgeSquareSum(1000) == True
    assert Solution().judgeSquareSum(100000000) == True
