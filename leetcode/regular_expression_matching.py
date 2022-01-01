#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         if len(p) == 0: 
#             return len(s) == 0

#         match = s and (p[0] == '.' or p[0] == s[0])

#         if len(p) >= 2 and p[1] == "*":
#             return self.isMatch(s, p[2:]) or match and self.isMatch(s[1:], p)
#         else:
#             return match and self.isMatch(s[1:], p[1:])

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         cache = {}
#         def dp(i, j) -> bool:
#             if (i, j) not in cache:
#                 if len(p) == j:
#                     ans = i == len(s)
#                 else:
#                     match = i < len(s) and (p[j] == '.' or p[j] == s[i])

#                     if len(p) >= j + 2 and p[j + 1] == "*":
#                         ans = dp(i, j+2) or match and dp(i + 1, j)
#                     else:
#                         ans = match and dp(i + 1, j + 1)
#                 cache[(i, j)] = ans
#             return cache[(i, j)]

#         return dp(0, 0)

class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                match = i < len(s) and (p[j] == '.' or p[j] == s[i])

                if j+1 < len(p) and p[j+1] == "*":
                    dp[i][j] = dp[i][j+2] or match and dp[i+1][j]
                else:
                    dp[i][j] = match and dp[i+1][j+1]
        return dp[0][0]
        
if __name__ == '__main__':
    s = Solution()
    assert s.isMatch("aaa", "ab*a*c*a")
    assert not s.isMatch("aaa", "aaaa")
    assert not s.isMatch("aaab", "a*ba")
    assert not s.isMatch("aa", "a")
    assert s.isMatch("aa", "a*")
    assert s.isMatch("aaa", "a*a")
    assert s.isMatch("ab", ".*")
    assert s.isMatch("aab", "c*a*b")
    assert not s.isMatch("mississippi", "mis*is*p*.")
    assert s.isMatch("mississippi", "mis*is*ip*.")