#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

import collections, heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        queue, graph, dt = [(0, K)], collections.defaultdict(list), {}
        for u, v, w in times:
            graph[u].append((v, w))

        while queue:
            time, vertex = heapq.heappop(queue)
            if vertex not in dt:
                dt[vertex] = time
                for v, w in graph[vertex]:
                    heapq.heappush(queue, (time + w, v))

        time = max(dt.values())
        return time if len(dt) == N else -1

# class Solution:
#     def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
#         dt, graph, seen = {}, collections.defaultdict(list), {}
#         for u, v, w in times:
#             graph[u].append((v, w))
#             dt[u], dt[v] = float('inf'), float('inf')
#             seen[u], seen[v] = False, False
#         if len(dt) < N: return -1
#         dt[K] = 0
#         while True:
#             vertex, min_distance = 0, float('inf')
#             for num in graph:
#                 if not seen[num] and dt[num] < min_distance:
#                     min_distance, vertex = dt[num], num
#             if vertex == 0: break
#             seen[vertex] = True
#             for v, w in graph[vertex]:
#                 dt[v] = min(dt[vertex] + w, dt[v])

#         time = max(dt.values())
#         return time if time != float('inf') else -1

# Queue
# class Solution:
#     def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
#         dt, graph, queue = {}, collections.defaultdict(list), [(0, K)]
#         for u, v, w in times:
#             graph[u].append((v, w))
#             dt[u], dt[v] = float('inf'), float('inf')
#         if len(dt) < N: return -1
        
#         while queue:
#             time, vertex = queue.pop(0)
#             if time < dt[vertex]:
#                 dt[vertex] = time
#                 for v, w in graph[vertex]:
#                     queue.append((time + w, v))

#         time = max(dt.values())
#         return time if time != float('inf') else -1

if __name__ == '__main__':
    print(Solution().networkDelayTime([[1,2,1],[2,1,3]], 2, 2))
    # print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
    # print(Solution().networkDelayTime([[1,2,1],[2,3,1],[3,4,1]], 4, 2))
    # print(Solution().networkDelayTime([[1,2,1],[2,3,7],[1,3,4],[2,1,2]], 4, 1))
    print(Solution().networkDelayTime([
        [4,2,76],
        [1,3,79],
        [3,1,81],
        [4,3,30],
        [2,1,47],
        [1,5,61],
        [1,4,99],
        [3,4,68],
        [3,5,46],
        [4,1,6],
        [5,4,7],
        [5,3,44],
        [4,5,19],
        [2,3,13],
        [3,2,18],
        [1,2,0],
        [5,1,25],
        [2,5,58],
        [2,4,77],
        [5,2,74]], 5, 3))
    