#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# class Solution:
    
#     def longestPalindrome(self, s: str) -> str:
#         def palindrome(l, r) -> (int, int):
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 l, r = l - 1, r + 1
#             return l + 1, r - l - 1

#         start, length = 0, 0
#         for i in range(len(s)):
#             s1 = palindrome(i, i)
#             if s1[1] > length: start, length = s1

#             s2 = palindrome(i, i+1)
#             if s2[1] > length: start, length = s2
#         return s[start : start + length]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, mid = '', len(s) // 2
        for i in range(mid, -1, -1):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i + 1)

            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2

            if i < len(res) // 2:
                break

        for i in range(mid + 1, len(s)):
            s1 = self.palindrome(s, i, i)            
            s2 = self.palindrome(s, i, i + 1)

            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2

            if i + 1 >= len(s) - len(res) // 2:
                break

        return res
    
    def palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1: r]

if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("abba"))
    print(Solution().longestPalindrome("a"))