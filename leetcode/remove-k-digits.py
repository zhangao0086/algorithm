from mimetypes import init
import re


#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for item in num:
            while k and stack and stack[-1] > item:
                stack.pop()
                k -= 1
            if stack or item != '0':
                stack.append(item)
        while stack and k > 0:
            stack.pop()
            k -= 1
        
        return "0" if not stack else "".join(stack)

if __name__ == '__main__':
    assert Solution().removeKdigits("1432219", 3) == "1219"
    assert Solution().removeKdigits("10200", 1) == "200"
    assert Solution().removeKdigits("10", 2) == "0"
    assert Solution().removeKdigits("1", 1) == "0"