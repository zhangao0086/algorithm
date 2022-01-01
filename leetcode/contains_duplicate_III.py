#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # # 1. 暴力解法
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, min(len(nums), i + k + 1)):
        #         if abs(nums[i] - nums[j]) <= t:
        #             return True
        # return False

        # 2. 桶
        if t < 0: return False

        buckets = {}
        for i in range(len(nums)):
            bucket = nums[i] // (t + 1)
            if bucket in buckets:
                return True
            
            if bucket - 1 in buckets:
                if nums[i] - buckets[bucket - 1] <= t:
                    return True

            if bucket + 1 in buckets:
                if buckets[bucket + 1] - nums[i] <= t:
                    return True

            buckets[bucket] = nums[i]
            if i >= k:
                del buckets[nums[i - k] // (t + 1)]

        return False

if __name__ == '__main__':
    print(Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))