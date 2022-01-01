#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        if result == target: return result
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == target:
                    return temp

                if abs(result - target) > abs(temp - target):
                    result = temp

                if temp > target:
                    k -= 1
                elif temp < target:
                    j += 1

        return result


if __name__ == '__main__':
    print(Solution().threeSumClosest([0,2,1,-3], 1))
