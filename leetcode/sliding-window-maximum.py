#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

import heapq
from collections import deque
from typing import List

class Solution:

    # heap
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     q = [(-nums[i], i) for i in range(k)]
    #     heapq.heapify(q)

    #     ans = [-q[0][0]]
    #     for i in range(k, len(nums)):
    #         heapq.heappush(q, (-nums[i], i))
    #         while q[0][1] <= i - k:
    #             heapq.heappop(q)
    #         ans.append(-q[0][0])
    #     return ans

    # stack
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     stack = []
    #     for i in range(k):
    #         while stack and nums[stack[-1]] <= nums[i]:
    #             stack.pop()
    #         stack.append(i)

    #     ans = [nums[stack[0]]]
    #     for i in range(k, len(nums)):
    #         while stack and nums[stack[-1]] <= nums[i]:
    #             stack.pop()
    #         stack.append(i)

    #         while stack[0] <= i - k:
    #             stack.pop(0)
    #         ans.append(nums[stack[0]])
    #     return ans

    # deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        for i in range(k):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            stack.append(i)

        ans = [nums[stack[0]]]
        for i in range(k, len(nums)):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            stack.append(i)

            while stack[0] <= i - k:
                stack.popleft()
            ans.append(nums[stack[0]])
        return ans

if __name__ == '__main__':
    assert Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert Solution().maxSlidingWindow([1], 1) == [1]
    assert Solution().maxSlidingWindow([1,-1], 1) == [1,-1]
    assert Solution().maxSlidingWindow([9,11], 2) == [11]
    assert Solution().maxSlidingWindow([4,-2], 2) == [4]