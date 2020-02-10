#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        if length < 4: return []
        nums.sort()

        return self.kSum(nums, target, 4, 0)

    def kSum(self, nums: List[int], target, k, low) -> List[List[int]]:
        results = []
        if k == 2:
            high = len(nums) - 1
            while low < high:
                sum = nums[low] + nums[high]
                if sum == target:
                    results.append([nums[low], nums[high]])

                    low += 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1

                    high -= 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif sum < target:
                    low += 1
                else:
                    high -= 1
        else:
            for i in range(low, len(nums)):
                value = nums[i]
                if i > low and nums[i - 1] == value: continue # 避免重复
                if value + nums[-1] * (k - 1) < target: continue # 避免过小
                if value * k > target: break # 避免过大
                results += [[value] + suffix for suffix in self.kSum(nums, target - value, k - 1, i + 1)]

        return results

if __name__ == '__main__':
    print(Solution().fourSum([1, 0, -1, 0, -2, 2, 0, 0], 0))
    print(Solution().fourSum([-493,-482,-482,-456,-427,-405,-392,-385,-351,-269,-259,-251,-235,-235,-202,-201,-194,-189,-187,-186,-180,-177,-175,-156,-150,-147,-140,-122,-112,-112,-105,-98,-49,-38,-35,-34,-18,20,52,53,57,76,124,126,128,132,142,147,157,180,207,227,274,296,311,334,336,337,339,349,354,363,372,378,383,413,431,471,474,481,492], 6189))
