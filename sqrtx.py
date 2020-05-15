#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         left, right = 1, x
#         while left <= right:
#             num = (left + right) // 2
#             square = num * num
#             if square == x:
#                 return num
#             elif square > x:
#                 right = num - 1
#             else:
#                 left = num + 1
#         return right

class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r > x:
            r = int((r + x/r) // 2)
        return r

if __name__ == '__main__':
    assert Solution().mySqrt(0) == 0
    assert Solution().mySqrt(1) == 1
    assert Solution().mySqrt(2) == 1
    assert Solution().mySqrt(3) == 1
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(5) == 2
    assert Solution().mySqrt(6) == 2
    assert Solution().mySqrt(7) == 2
    assert Solution().mySqrt(8) == 2
    assert Solution().mySqrt(9) == 3
    assert Solution().mySqrt(2147395599) == 46339