#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        res = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                res += 2 ** (right - left)
                left += 1
            else:
                right -= 1
        return res % (10 ** 9 + 7)

if __name__ == '__main__':
    solution = Solution()
    assert solution.numSubseq([3, 5, 6, 7], 9) == 4
    assert solution.numSubseq([3, 3, 6, 8], 10) == 6
    assert solution.numSubseq([2, 3, 3, 4, 6, 7], 12) == 61
    assert solution.numSubseq([5, 2, 4, 1, 7, 6, 8], 16) == 127
    assert solution.numSubseq([14, 4, 6, 6, 20, 8, 5, 6, 8, 12, 6, 10, 14, 9, 17, 16, 9, 7, 14, 11, 14, 15, 13, 11, 10, 18, 13, 17, 17, 14, 17, 7, 9, 5, 10, 13, 8, 5, 18, 20, 7, 5, 5, 15, 19, 14], 22) == 272187084