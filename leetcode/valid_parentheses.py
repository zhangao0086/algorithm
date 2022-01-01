#!/usr/bin/python3
# -*-coding:utf-8-*-
__author__ = "Bannings"

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')', '[':']', '{':'}'}
        stack = []
        for char in s:
            closing = mapping.get(char)
            if closing:
                stack.append(closing)
            elif not (stack and stack.pop() == char):
                return False
        
        return not stack

if __name__ == '__main__':
    print(Solution().isValid("()"))
    print(Solution().isValid("([{}])"))
    print(Solution().isValid("({}])"))