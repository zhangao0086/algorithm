#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = [letter.lower() for letter in s if letter.isalnum()]
#         return s == s[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [letter.lower() for letter in s if letter.isalnum()]
        for i in range(len(s)//2):
            if s[i] != s[~i]: return False
        return True

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = [letter.lower() for letter in s if letter.isalnum()]
#         return all([s[i]==s[~i] for i in range(len(s)//2)])

if __name__ == '__main__':
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True
    assert Solution().isPalindrome("race a car") == False