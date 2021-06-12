#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum(int(digit)**2 for digit in str(n))
        return n == 1

if __name__ == '__main__':
    assert Solution().isHappy(19)
    assert not Solution().isHappy(2)