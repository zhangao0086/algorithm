#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        length = len(envelopes)

        if not length:
            return 0

        def quick_sort(envelopes: List[List[int]], left: int, right: int):
            if left >= right:
                return

            def partition(envelopes: List[List[int]], left: int, right: int) -> int:
                pivot_index = left
                pivot = envelopes[pivot_index]

                while left < right:
                    while left < right and (envelopes[right][0] > pivot[0] or (envelopes[right][0] == pivot[0] and envelopes[right][1] < pivot[1])):
                        right -= 1

                    while left < right and (envelopes[left][0] < pivot[0] or (envelopes[left][0] == pivot[0] and envelopes[left][1] >= pivot[1])):
                        left += 1

                    if left < right:
                        envelopes[left], envelopes[right] = envelopes[right], envelopes[left]

                envelopes[left], envelopes[pivot_index] = envelopes[pivot_index], envelopes[left]
                return left


            middle = partition(envelopes, left, right)
            quick_sort(envelopes, left, middle - 1)
            quick_sort(envelopes, middle + 1, right)
        
        # quick_sort(envelopes, 0, length - 1)
        envelopes.sort(key=lambda x: (x[0],-x[1]))

        # # dp 版
        # dp = [1] * length
        # for i in range(1, length):
        #     for j in range(i):
        #         if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # 
        # return max(dp)

        def binary_search(nums: [int], target: int, low: int, high: int) -> int:
            while low < high:
                middle = (high + low) // 2
                if nums[middle] < target:
                    low = middle + 1
                else:
                    high = middle

            return low

        tails = [None] * length
        max_count = 0
        for _, h in envelopes:
            position = binary_search(tails, h, 0, max_count)
            tails[position] = h
            max_count += position == max_count

        return max_count

if __name__ == '__main__':
    print(Solution().maxEnvelopes([[1,15],[7,18],[7,6],[7,100],[2,200],[17,30],[17,45],[3,5],[7,8],[3,6],[3,10],[7,20],[17,3],[17,45]]))