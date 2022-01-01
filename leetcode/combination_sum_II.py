#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.recursive(0, candidates, target, result, [])
        return result
    
    def recursive(self, start: int, candidates: List[int], target: int, result: List[List[int]], path: List[int]):
        if target == 0:
            result += [path]
            return

        for index in range(start, len(candidates)):
            candidate = candidates[index]

            if index > start and candidate == candidates[index - 1]:
                continue

            if candidate > target:
                return
                
            self.recursive(index + 1, candidates, target - candidate, result, path + [candidate])

if __name__ == '__main__':
    print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))