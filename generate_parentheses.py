#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(item: str, left: int, right: int):
            if len(item) == 2 * n:
                ans.append(item)
                return
            if left < n:
                backtrack(f"{item}(", left + 1, right)
            if right < left:
                backtrack(f"{item})", left, right + 1)
            pass
        backtrack("", 0, 0)
        return ans

if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(4))