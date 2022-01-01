#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            key = "".join(sorted(word))
            anagrams = ans.get(key, [])
            anagrams.append(word)
            ans[key] = anagrams
        return list(ans.values())

if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(Solution().groupAnagrams(["a"]))