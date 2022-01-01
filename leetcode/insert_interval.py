#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans, index, n = [], 0, len(intervals)
        while index < n and intervals[index][1] < newInterval[0]:
            ans.append(intervals[index])
            index += 1
        
        ans.append(newInterval)

        while index < n:
            if intervals[index][0] <= ans[-1][1]:
                ans[-1][0] = min(ans[-1][0], intervals[index][0])
                ans[-1][1] = max(ans[-1][1], intervals[index][1])
            else:
                ans.append(intervals[index])
            index += 1
        return ans

if __name__ == '__main__':
    print(Solution().insert([[1,3],[6,9]], [2,5]))
    print(Solution().insert([[1,3],[6,9]], [2,6]))
    print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    print(Solution().insert([], [5,7]))
    print(Solution().insert([[1,5]], [2,3]))
    print(Solution().insert([[1,5]], [2,7]))
    print(Solution().insert([[1,5]], [6,8]))
    print(Solution().insert([[1,5]], [0,3]))
    print(Solution().insert([[1,5]], [0,0]))
    print(Solution().insert([[3,5],[12,15]], [6,6]))