#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2

if __name__ == '__main__':
    assert Solution().removePalindromeSub("ababa") == 1
    assert Solution().removePalindromeSub("abb") == 2
    assert Solution().removePalindromeSub("baabb") == 2
    assert Solution().removePalindromeSub("abbaaaab") == 2