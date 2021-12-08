#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
#         ans = []
#         for i in range(len(boxes)):
#             curr = 0
#             for j in range(len(boxes)):
#                 if j != i and boxes[j] == "1":
#                     curr += abs(j-i)
#             ans.append(curr)
#         return ans

# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
#         ans = [0] * len(boxes)
#         for i in range(len(boxes)):
#             if boxes[i] == "1":
#                 for j in range(len(boxes)):
#                     ans[j] += abs(i-j)
#         return ans

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        count, steps = 0, 0
        for i in range(n):
            ans[i] += steps
            count += int(boxes[i])
            steps += count

        count, steps = 0, 0
        for i in reversed(range(n)):
            ans[i] += steps
            count += int(boxes[i])
            steps += count
        return ans

if __name__ == '__main__':
    assert Solution().minOperations("110") == [1,1,3]
    assert Solution().minOperations("001011") == [11,8,5,4,3,4]