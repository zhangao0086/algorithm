#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:

    # def myPow(self, x: float, n: int) -> float:
    #     """
    #     Exponentiation by squaring using recursion
    #     """
    #     def pow(n):
    #         if n == 0: return 1
    #         ans = pow(n // 2)
    #         return ans * ans * (1 if n % 2 == 0 else x)
    #     return pow(n) if n > 0 else 1 / pow(-n)

    def myPow(self, x: float, n: int) -> float:
        """
        Exponentiation by squaring using iteration
        """
        def pow(n):
            ans = 1
            x_contribute = x
            while n:
                if n % 2 == 1:
                    ans *= x_contribute
                x_contribute *= x_contribute
                n //= 2
            return ans
        return pow(n) if n > 0 else 1 / pow(-n)

if __name__ == '__main__':
    import math
    # assert Solution().myPow(0.44528, 0) == 1
    assert Solution().myPow(2, 10) == 1024
    assert math.isclose(Solution().myPow(2.1, 3), 9.261)
    assert Solution().myPow(2, -2) == 0.25