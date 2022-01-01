#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         if not s and not p: return True
#         if not p: return False
#         if not s: return len(p) - p.count('*') == 0
        
#         first = s[0]
#         if p[0] == '*':
#             return any([
#                 self.isMatch(s[1:], p),
#                 self.isMatch(s[1:], p[1:]),
#                 self.isMatch(s, p[1:]),
#             ])
#         elif p[0] == '?' or p[0] == first:
#             return self.isMatch(s[1:], p[1:])
#         return False

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
#         dp[0][0] = True
#         for i in range(len(p)):
#             if p[i] != '*':
#                 break
#             dp[0][i+1] = True
        
#         for i in range(1, len(s) + 1):
#             for j in range(1, len(p) + 1):
#                 if p[j-1] in {s[i-1], '?'}:
#                     dp[i][j] = dp[i-1][j-1]
#                 elif p[j - 1] == '*':
#                     dp[i][j] = dp[i-1][j] or dp[i][j-1]
#         return dp[-1][-1]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, m = 0, len(s)
        j, n = 0, len(p)
        i_star, j_star = -1, -1

        while i < m:
            if j < n and p[j] == '*':
                i_star, j_star = i, j
                j += 1
            elif j < n and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif i_star > -1:
                i, j = i_star + 1, j_star + 1
                i_star += 1
            else: return False
        while j < n and p[j] == '*': j += 1
        return j == n

if __name__ == '__main__':
    assert Solution().isMatch("acde", "a*d*") == True
    assert Solution().isMatch("acde", "a*cd*") == True
    assert Solution().isMatch("", "******") == True
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "*") == True
    assert Solution().isMatch("cb", "?a") == False
    assert Solution().isMatch("adceb", "*a*b") == True
    assert Solution().isMatch("acdcb", "a*c?b") == False