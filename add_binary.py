#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, ans = 0 , ''
        for i in range(max(len(a), len(b))):
            carry += ord(a[len(a) - i - 1]) - ord('0') if i < len(a) else 0
            carry += ord(b[len(b) - i - 1]) - ord('0') if i < len(b) else 0
            
            ans = chr(carry % 2 + ord('0')) + ans
            carry //= 2
        return ans if carry == 0 else '1' + ans

if __name__ == '__main__':
    assert Solution().addBinary("11", "1") == "100"
    assert Solution().addBinary("1010", "1011") == "10101"