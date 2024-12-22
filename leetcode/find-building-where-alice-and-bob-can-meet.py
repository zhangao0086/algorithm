#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

import heapq
from typing import List

class Solution:

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(heights), len(queries)
        ans = [-1] * q
        deferred = [[] for _ in range(n)]
        pq = []

        for i in range(q):
            a, b = queries[i]
            a, b = min(a, b), max(a, b)

            if a == b or heights[a] < heights[b]:
                ans[i] = b
            else:
                deferred[b].append((heights[a], i))
        
        for i in range(n):        
            for query in deferred[i]:
                heapq.heappush(pq, query)
            
            while pq and pq[0][0] < heights[i]:
                ans[pq[0][1]] = i
                heapq.heappop(pq)
        
        return ans

    # Time Limit Exceeded
    # def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # next_higher = [n] * n
        # stack = []
        
        # for i in range(n-1, -1, -1):
        #     while stack and heights[stack[-1]] <= heights[i]:
        #         stack.pop()
        #     if stack:
        #         next_higher[i] = stack[-1]
        #     stack.append(i)

        # ans = []
        # for i, j in queries:
        #     i, j = min(i, j), max(i, j)
        #     if i == j or heights[i] < heights[j]:
        #         ans.append(j)
        #         continue
                
        #     target = heights[i]
        #     k = next_higher[j]
        #     while k < n and heights[k] <= target:
        #         k = next_higher[k]
        #     ans.append(k if k < n else -1)

        # return ans
    
        # Time Limit Exceeded
#     def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # ans = []
        # for i, j in queries:
        #     i, j = min(i, j), max(i, j)
        #     if heights[i] < heights[j] or i == j:
        #         ans.append(j)
        #         continue
        #     for k in range(j+1, n):
        #         if heights[k] > heights[i]:
        #             ans.append(k)
        #             break
        #     else:
        #         ans.append(-1)


if __name__ == '__main__':
#     assert Solution().leftmostBuildingQueries([3,1,2,4], [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]) == [0,3,3,3,3,1,2,3,3,2,2,3,3,3,3,3]
    
#     assert Solution().leftmostBuildingQueries([1,2,1,2,1,2]
# , [
#     [0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,1],
#     [1,2],[1,3],[1,4],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]]) == [0,1,3,3,5,5,1,1,-1,-1,-1,-1,3,-1,2,3,5,5,3,-1,3,3,-1,-1,5,-1,5,-1,4,5,5,-1,5,-1,5,5]
    assert Solution().leftmostBuildingQueries([6, 4, 8, 5, 2, 7], [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]) == [2, 5, -1, 5, 2]
