#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = []
        while n > 0:
            n -= 1
            d = min(k - n, 26)
            result.append(chr(ord('a') + d - 1))
            k -= d
        return ''.join(result[::-1])

if __name__ == '__main__':
    assert Solution().getSmallestString(3, 27) == "aay"
    assert Solution().getSmallestString(5, 73) == "aaszz"
