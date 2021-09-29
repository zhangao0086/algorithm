#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)
        if length == 1: return ""
        
        for i in range(length // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        
        return palindrome[:-1] + 'b'

if __name__ == '__main__':
    assert Solution().breakPalindrome("abccba") == "aaccba"
    assert Solution().breakPalindrome("a") == ""
    assert Solution().breakPalindrome("aa") == "ab"
    assert Solution().breakPalindrome("aba") == "abb"