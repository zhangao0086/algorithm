#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List
import collections

# class Solution:
    # def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
    #     piles, num = [], 0
    #     for i in range(0, len(A)):
    #         delete_count = 0
    #         for j in range(0, len(piles)):
    #             pile = piles[j - delete_count]
    #             if not pile:
    #                 continue
    #             if len(pile) < K:
    #                 pile.add(A[i])
    #             elif len(pile) == K:
    #                 num += 1
    #                 if A[i] not in pile:
    #                     del piles[j - delete_count]
    #                     delete_count += 1

    #         piles.append(set())
    #         piles[-1].add(A[i])
    #     print(num, piles)
    #     return num + len([pile for pile in piles if len(pile) == K])

class Window:
    def __init__(self):
        self.count = collections.Counter()
        self.nonzero = 0

    def add(self, x):
        self.count[x] += 1
        if self.count[x] == 1:
            self.nonzero += 1

    def remove(self, x):
        self.count[x] -= 1
        if self.count[x] == 0:
            self.nonzero -= 1

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        window1 = Window()
        window2 = Window()
        ans = left1 = left2 = 0

        for x in A:
            window1.add(x)
            window2.add(x)

            while window1.nonzero > K:
                window1.remove(A[left1])
                left1 += 1

            while window2.nonzero >= K:
                window2.remove(A[left2])
                left2 += 1

            ans += left2 - left1

        return ans


# class Solution:
#     def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
#         def atMostK(A: List[int], K: int) -> int:
#             count = [0] * (len(A) + 1)
#             ans = left = 0
#             for right in range(len(A)):
#                 count[A[right]] += 1
#                 if count[A[right]] == 1: K -= 1
#                 while K < 0:
#                     count[A[left]] -= 1
#                     if count[A[left]] == 0: K += 1
#                     left += 1
#                 ans += right - left + 1
#             return ans
#         return atMostK(A, K) - atMostK(A, K - 1)

if __name__ == '__main__':
    print(Solution().subarraysWithKDistinct([1,2,3], 2))
    print(Solution().subarraysWithKDistinct([1,2,1,2,3], 1))
    print(Solution().subarraysWithKDistinct([1,2,1,2,3], 2))
    print(Solution().subarraysWithKDistinct([1,2,1,3,4], 3))