#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        table = dict()
        for i in nums1:
            for j in nums2:
                table[i+j] = table.get(i+j, 0) + 1

        ans = sum(table.get(-l-k, 0)for k in nums4 for l in nums3)
        return ans

if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    assert Solution().fourSumCount(nums1, nums2, nums3, nums4) == 2

    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]
    assert Solution().fourSumCount(nums1, nums2, nums3, nums4) == 1