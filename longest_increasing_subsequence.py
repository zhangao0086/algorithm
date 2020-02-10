#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
            
        # # dp
        # length = len(nums)
        # dp = [1] * length
        # for i in range(1, length):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[j] + 1, dp[i])

        # dp with binary search
        length = len(nums)
        dp = [None] * length
        dp_length = 0

        def binary_search(num: int, length: int) -> int:
            low, high = 0, length
            while low < high:
                middle = low + (high - low) // 2

                if dp[middle] == num:
                    return middle
                elif dp[middle] < num:
                    low = middle + 1
                else:
                    high = middle

            return low

        for num in nums:
            position = binary_search(num, dp_length)
            dp[position] = num
            dp_length += dp[dp_length] == num

        print(dp)
        return dp_length

if __name__ == '__main__':
    print(Solution().lengthOfLIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))