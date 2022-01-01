#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        
        return dp[-1]

if __name__ == '__main__':
    assert Solution().wordBreak("leetcode", ["leet","code"]) == True
    assert Solution().wordBreak("applepenapple", ["apple","pen"]) == True
    assert Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"]) == False