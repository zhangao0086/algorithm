#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# class Solution:
#     def numDecodings(self, s: str, start: int = 0) -> int:
#         if not s: return 0
        
#         if start == len(s): return 1
#         if s[start] == '0': return 0

#         ans = self.numDecodings(s, start + 1)
        
#         if start < len(s) - 1 and int(s[start:start+2]) < 27:
#             ans += self.numDecodings(s, start + 2)

#         return ans

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] != '0':
                dp[i] = dp[i+1]
                if i < len(s) - 1 and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                    dp[i] += dp[i + 2]
        return dp[0]

if __name__ == '__main__':
    # assert Solution().numDecodings("12") == 2
    assert Solution().numDecodings("1201234") == 3