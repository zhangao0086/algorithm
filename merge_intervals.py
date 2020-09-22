#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for interval in sorted(intervals, key=lambda interval: interval[0]):
            if ans and interval[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval)
        return ans

if __name__ == '__main__':
    print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
    print(Solution().merge([[1,4],[4,5]]))
    print(Solution().merge([[1,4],[0,4]]))