#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans, nums = 0, set(nums)
        for num in nums:
            if num - 1 not in nums:
                current = num + 1
                while current in nums:
                    current += 1
                ans = max(ans, current - num)
        return ans

if __name__ == '__main__':
    assert Solution().longestConsecutive([100,4,200,1,3,2,0,-1]) == 6
    assert Solution().longestConsecutive([9,1,-3,2,4,8,3,-1,6,-2,-4,7]) == 4
    assert Solution().longestConsecutive([100,4,200,1,3,2]) == 4
    assert Solution().longestConsecutive([100,4,200,1,2,2]) == 2
    assert Solution().longestConsecutive([100,4,200,1,3,2,0]) == 5