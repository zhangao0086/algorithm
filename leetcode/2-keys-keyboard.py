#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        for i in range(2, n):
            if n % i == 0:
                return i + self.minSteps(n // i)
        return n

if __name__ == '__main__':
    assert Solution().minSteps(3) == 3
    assert Solution().minSteps(1) == 0