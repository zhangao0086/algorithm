#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

# class Solution:
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     ans = 0
        
    #     lessFromLeft = [0] * len(heights)
    #     lessFromLeft[0] = -1
    #     for i in range(1, len(heights)):
    #         p = i - 1
    #         while p >= 0 and heights[p] >= heights[i]:
    #             p = lessFromLeft[p]
    #         lessFromLeft[i] = p
        
    #     lessFromRight = [0] * len(heights)
    #     lessFromRight[len(heights)-1] = len(heights)
    #     for i in range(len(heights) - 2, -1, -1):
    #         p = i + 1
    #         while p < len(heights) and heights[p] >= heights[i]:
    #             p = lessFromRight[p]
    #         lessFromRight[i] = p

    #     for i in range(len(heights)):
    #         ans = max(ans, heights[i] * (lessFromRight[i] - lessFromLeft[i] - 1))

    #     return ans

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans, stack, heights = 0, [0], [0] + heights + [0]
        for i in range(1, len(heights)):
            while heights[stack[-1]] > heights[i]:
                ans = max(ans, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        return ans

if __name__ == '__main__':
    assert Solution().largestRectangleArea([2,1,5,6,2,3]) == 10
    assert Solution().largestRectangleArea([2,4]) == 4
    assert Solution().largestRectangleArea([0]) == 0
    assert Solution().largestRectangleArea([]) == 0