#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp, tp = 0, 0
        while sp < len(s) and tp < len(t):
            sp += int(s[sp] == t[tp])
            tp += 1
        return sp == len(s)

if __name__ == '__main__':
    assert Solution().isSubsequence("abc", "ahbgdc") == True
    assert Solution().isSubsequence("axc", "ahbgdc") == False