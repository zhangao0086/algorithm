#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = {}
        end = minSize

        while end <= len(s):
            substring = s[end-minSize:end]
            letters_count = len(set(substring))
            if letters_count <= maxLetters:
                counts[substring] = counts.get(substring, 0) + 1
            end += 1
        return max(counts.values()) if counts else 0

if __name__ == '__main__':
    print(Solution().maxFreq("", 2, 3, 4))
    print(Solution().maxFreq("aababcaab", 2, 3, 4))