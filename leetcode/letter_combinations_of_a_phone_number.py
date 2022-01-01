#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    # map = {
    #     '2': 'abc',
    #     '3': 'def',
    #     '4': 'ghi',
    #     '5': 'jkl',
    #     '6': 'mno',
    #     '7': 'pqrs',
    #     '8': 'tuv',
    #     '9': 'wxyz',
    # }
    
    # 数组比字典有更少的内存占用
    map = [ 'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz' ]

    # 递归
    # def letterCombinations(self, digits: str) -> List[str]:
    #     ans = []
    #     def recursive(letters, remain):
    #         if len(remain) == 0:
    #             ans.append(letters)
    #         else:
    #             for letter in Solution.map[remain[0]]:
    #                 recursive(letters + letter, remain[1:])

    #     if digits: recursive('', digits)
    #     return ans

    # BFS，基于栈
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        ans = [""]
        while ans and len(ans[0]) != len(digits):
            letter = ans.pop(0)
            for char in Solution.map[int(digits[len(letter)])-2]:
                ans.append(letter + char)
        return ans

if __name__ == '__main__':
    print(Solution().letterCombinations(''))
    print(Solution().letterCombinations('23'))