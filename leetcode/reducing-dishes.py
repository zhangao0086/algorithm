#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List
from itertools import accumulate
# from functools import cache

# class Solution:
#     def maxSatisfaction(self, satisfaction: List[int]) -> int:
#         satisfaction.sort()

#         @cache
#         def _maxSatisfaction(i: int, level: int) -> int:
#             if len(satisfaction) == i: return 0
#             return max(
#                 satisfaction[i] * level + _maxSatisfaction(i + 1, level + 1),
#                 _maxSatisfaction(i + 1, level)
#             )

#         return _maxSatisfaction(0, 1)

# class Solution:
#     def maxSatisfaction(self, satisfaction: List[int]) -> int:
#         satisfaction.sort()
#         ans, curr = 0, 0
#         while satisfaction and satisfaction[-1] + curr > 0:
#             curr += satisfaction.pop()
#             ans += curr
        
#         return ans

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        return max(0, max(accumulate(accumulate(sorted(satisfaction, reverse=True)))))

if __name__ == '__main__':
    assert Solution().maxSatisfaction([-1,-8,0,5,-9]) == 14
    assert Solution().maxSatisfaction([4,3,2]) == 20
    assert Solution().maxSatisfaction([-1,-4,-5]) == 0
    assert Solution().maxSatisfaction([-2,5,-1,0,3,-3]) == 35