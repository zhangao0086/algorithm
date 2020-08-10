#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    # # 二维数组版本的 KMP
#     def strStr(self, haystack: str, needle: str) -> int:
#         m = len(needle)
#         if m == 0: return 0
        
#         # 构建状态表
#         dp = [[0] * (ord('z') - ord('a') + 1) for _ in range(m)]
#         dp[0][ord(needle[0]) - ord('a')] = 1
#         x = 0
#         for j in range(1, m):
#             for c in range(ord('z') - ord('a')):
#                 if needle[j] == chr(ord('a') + c):
#                     dp[j][c] = j + 1
#                 else:
#                     dp[j][c] = dp[x][c]
#             x = dp[x][ord(needle[j]) - ord('a')]

#         # 开始状态推进
#         j = 0
#         for i, s in enumerate(haystack):
#             j = dp[j][ord(s) - ord('a')]
#             if j == m: return i - m + 1
#         return -1

    # 传统的 KMP
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0: return 0
        if n == 0: return -1

        # 构建状态回退表
        dp = [0] * m
        j = 0
        for i in range(1, m):
            if j > 0 and needle[i] != needle[j]:
                j = dp[j-1]
            
            if needle[i] == needle[j]:
                j += 1
                dp[i] = j
        
        # 开始匹配
        i, j = 0, 0
        while i < n:
            while j > 0 and haystack[i] != needle[j]:
                j = dp[j-1]
            
            if haystack[i] == needle[j]:
                j += 1
            i += 1
            if j == m: return i - j
            
        return -1

    # # 双指针暴力解法
    # def strStr(self, haystack: str, needle: str) -> int:
    #     n, m = len(haystack), len(needle)
    #     if m == 0: return 0
    #     if n == 0: return -1

    #     p1, p2, curr_len = 0, 0, 0
    #     while p1 < n and p2 < m:
    #         if haystack[p1] == needle[p2]:
    #             curr_len += 1
    #             p1 += 1
    #             p2 += 1
    #         else:
    #             p1 = p1 - curr_len + 1
    #             p2, curr_len = 0, 0
    #         if curr_len == m: return p1-p2
    #     return -1

if __name__ == '__main__':
    assert Solution().strStr("ababcab", "ababa") == -1
    assert Solution().strStr("ababca", "abc") == 2
    assert Solution().strStr("hello", "") == 0
    assert Solution().strStr("hello", "ll") == 2
    assert Solution().strStr("helloz", "z") == 5
    assert Solution().strStr("helloz", "lla") == -1
    assert Solution().strStr("helloz", "ell") == 1