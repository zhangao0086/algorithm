import imp
from mimetypes import init


#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans, gaps = 0, []
        n = len(costs)//2
        for a, b in costs:
            ans += a
            gaps.append(b-a)
        gaps.sort()
        for i in range(n):
            ans += gaps[i]
        return ans

if __name__ == '__main__':
    assert Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]) == 110