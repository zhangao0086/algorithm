#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        exist = [False] * len(words)
        for i in range(len(words)):
            if exist[i]: continue
            for j in range(len(words)):
                # if i != j and words[i] in words[j]:
                #     ans.append(words[i])
                #     break
                if i != j and not exist[j] and words[j] in words[i]:
                    ans.append(words[j])
                    exist[j] = True
        return ans

if __name__ == '__main__':
    print(Solution().stringMatching(["mass","as","hero","superhero"]))
    print(Solution().stringMatching(["leetcode","et","code"]))
    print(Solution().stringMatching([]))
    print(Solution().stringMatching(["leetcoder","leetcode","od","hamlet","am"]))
    print(Solution().stringMatching(["jak","yjakdn","tj","yyjakdn"]))