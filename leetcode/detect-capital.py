#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        isupper = word[-1].isupper()
        for i in range(len(word) - 2, -1, -1):
            if word[i].isupper() != isupper and (isupper or i != 0):
                return False
        return True

if __name__ == '__main__':
    assert Solution().detectCapitalUse("mL") == False
    assert Solution().detectCapitalUse("word") == True
    assert Solution().detectCapitalUse("Word") == True
    assert Solution().detectCapitalUse("woRd") == False