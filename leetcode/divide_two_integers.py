#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1: return 2147483647

        ans, abs_dividend, abs_divisor = 0, abs(dividend), abs(divisor)
        while abs_dividend >= abs_divisor:
            temp, remainder = abs_divisor, 1
            while temp << 1 <= abs_dividend:
                 temp <<= 1
                 remainder <<= 1
            abs_dividend -= temp
            ans += remainder
        return ans if (dividend > 0) == (divisor > 0) else -ans

if __name__ == '__main__':
    assert Solution().divide(10, 3) == 3
    assert Solution().divide(10, -3) == -3
    assert Solution().divide(-10, -3) == 3