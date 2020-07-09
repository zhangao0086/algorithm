#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def reverse(self, x: int) -> int:
        ans, y = 0, abs(x)
        boundary = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            if boundary // 10 - (y % 10) < ans: return 0
            ans = ans * 10 + y % 10
            y //= 10
        return ans if x > 0 else -ans

if __name__ == '__main__':
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(-214748364))
    print(Solution().reverse(2147483647))
    print(Solution().reverse(2147483646))
    print(Solution().reverse(2147483641))
    print(Solution().reverse(2147483642))