#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def numberOfSteps(self, num: int) -> int:
        if not num: return 0
        ans = 0
        while num:
            ans += 2 if (num & 1) else 1
            num >>= 1
        return ans - 1

if __name__ == '__main__':
    assert Solution().numberOfSteps(14) == 6
    assert Solution().numberOfSteps(8) == 4
    assert Solution().numberOfSteps(123) == 12