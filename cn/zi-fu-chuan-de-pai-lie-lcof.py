#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:

    # def permutation(self, s: str) -> List[str]:
    #     arr, ans = list(s), []
    #     def dfs(index: int):
    #         if index == len(s) - 1:
    #             ans.append(''.join(arr))
    #             return
    #         dic = set()
    #         for i in range(index, len(s)):
    #             if arr[i] in dic: continue
    #             dic.add(arr[i])
    #             arr[i], arr[index] = arr[index], arr[i]
    #             dfs(index + 1)
    #             arr[i], arr[index] = arr[index], arr[i]

    #     dfs(0)
    #     return ans

    def permutation(self, s: str) -> List[str]:
        """
        按顺序递推计算。
        以 "abc" 为例，先以 a、b 算出 "ab"、"ba"，
        再将 c 分别插入到"ab"和"ba"中。
        """
        visited = set(s[0])
        for i in range(1, len(s)):
            next_visited = set()
            for j in visited:
                for k in range(len(j) + 1):
                    cur = j[:k] + s[i] + j[k:]
                    next_visited.add(cur)
            visited = next_visited.copy()
        return list(visited)

if __name__ == '__main__':
    print(Solution().permutation("abc"))