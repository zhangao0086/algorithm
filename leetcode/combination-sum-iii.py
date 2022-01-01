#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int, begin = 1) -> List[List[int]]:
        if k == 1:
            return [[n]] if n < 10 and n >= begin else []
        else:
            ans = []
            for i in range(begin, 10):
                if k * i < n:
                    print(begin, k, n, i)
                    ans += [[i] + combination for combination in self.combinationSum3(k - 1, n - i, i + 1)]
            return ans

if __name__ == '__main__':
    assert Solution().combinationSum3(2, 18) == []
    assert Solution().combinationSum3(3, 7) == [[1,2,4]]
    assert Solution().combinationSum3(3, 9) == [[1,2,6],[1,3,5],[2,3,4]]
    assert Solution().combinationSum3(4, 1) == []
    assert Solution().combinationSum3(3, 2) == []
    assert Solution().combinationSum3(9, 45) == [[1,2,3,4,5,6,7,8,9]]