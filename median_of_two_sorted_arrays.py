#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:

    # 方法一：归并排序，然后取中位数
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     def _merge():
    #         nums = []
    #         nums1_begin, nums2_begin = 0, 0
    #         while nums1_begin < len(nums1) and nums2_begin < len(nums2):
    #             if nums1[nums1_begin] < nums2[nums2_begin]:
    #                 nums.append(nums1[nums1_begin])
    #                 nums1_begin += 1
    #             else:
    #                 nums.append(nums2[nums2_begin])
    #                 nums2_begin += 1
    #         while nums1_begin < len(nums1):
    #             nums.append(nums1[nums1_begin])
    #             nums1_begin += 1

    #         while nums2_begin < len(nums2):
    #             nums.append(nums2[nums2_begin])
    #             nums2_begin += 1
    #         return nums
        
    #     nums = _merge()
    #     if len(nums) % 2 == 0:
    #         return (nums[len(nums)//2] + nums[len(nums)//2-1]) / 2
    #     else:
    #         return nums[len(nums)//2]

    # 方法二：不需要做完整的排序，只需要记录两个中位数即可
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     nums1_begin, nums2_begin, half_len = 0, 0, (len(nums1) + len(nums2)) // 2
    #     left, right = 0, 0
    #     while half_len >= 0:
    #         half_len -= 1
    #         left = right
    #         if nums1_begin < len(nums1) and (nums2_begin >= len(nums2) or nums1[nums1_begin] < nums2[nums2_begin]):
    #             right = nums1[nums1_begin]
    #             nums1_begin += 1
    #         else:
    #             right = nums2[nums2_begin]
    #             nums2_begin += 1
        
    #     if (len(nums1) + len(nums2)) % 2 == 0:
    #         return (left + right) / 2
    #     else:
    #         return right

    # 方法三：取最小的第k个数
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     def _kth(nums1_begin, nums2_begin, k) -> int:
    #         len1 = len(nums1) - nums1_begin
    #         len2 = len(nums2) - nums2_begin
    #         if len1 == 0: return nums2[nums2_begin + k - 1]
    #         if len2 == 0: return nums1[nums1_begin + k - 1]
    #         if k == 1: return min(nums1[nums1_begin], nums2[nums2_begin])

    #         i = nums1_begin + min(k // 2, len1) - 1
    #         j = nums2_begin + min(k // 2, len2) - 1

    #         if nums1[i] < nums2[j]:
    #             return _kth(i + 1, nums2_begin, k - (i - nums1_begin + 1))
    #         else:
    #             return _kth(nums1_begin, j + 1, k - (j - nums2_begin + 1))

    #     total_len = len(nums1) + len(nums2)
    #     if total_len % 2 == 0:
    #         return (_kth(0, 0, total_len // 2) + _kth(0, 0, total_len // 2 + 1)) / 2
    #     else:
    #         return _kth(0, 0, total_len // 2 + 1)

    # 方法四：二分数组
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n: return self.findMedianSortedArrays(nums2, nums1)
        
        imin, imax = 0, m
        while imin <= imax:
            i = (imin + imax) // 2
            j = (m + n + 1) // 2 - i

            if i < m and nums2[j-1] > nums1[i]: # i 太小
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]: # i 太大
                imax = i - 1
            else: # i 合适
                if i == 0: max_left_num = nums2[j-1]
                elif j == 0: max_left_num = nums1[i-1]
                else: max_left_num = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 0:
                    if i == m: min_right_num = nums2[j]
                    elif j == n: min_right_num = nums1[i]
                    else: min_right_num = min(nums1[i], nums2[j])

                    return (max_left_num + min_right_num) / 2
                else:
                    return max_left_num
if __name__ == '__main__':
    assert Solution().findMedianSortedArrays([1,3], [2]) == 2
    assert Solution().findMedianSortedArrays([1,2], [3]) == 2
    assert Solution().findMedianSortedArrays([1,2], [3, 4]) == 2.5
    assert Solution().findMedianSortedArrays([3, 4], [1,2]) == 2.5
    assert Solution().findMedianSortedArrays([3], [-2, -1]) == -1