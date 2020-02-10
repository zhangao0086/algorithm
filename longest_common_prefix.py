#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        for char_index in range(len(strs[0])):
            char = strs[0][char_index]
            for index in range(1, len(strs)):
                if len(strs[index]) <= char_index or strs[index][char_index] != char:
                    return strs[0][:char_index]
        return strs[0]

if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
    print(Solution().longestCommonPrefix(["dog"]))
    print(Solution().longestCommonPrefix(["dog", "dog"]))
    print(Solution().longestCommonPrefix(["og", "dog"]))
    print(Solution().longestCommonPrefix([]))