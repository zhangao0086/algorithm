#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:

    class HeapSort:

        def __init__(self, length):
            self.length = length
            self.heap = []

        def add(self, num):
            if len(self.heap) < self.length:
                self.heap.append(num)
                self._up()
            elif num <= self.heap[0]:
                self.heap[0] = num
                self._down()

        def get(self) -> int:
            return self.heap[0]
        
        def pop(self) -> int:
            value = self.heap.pop(0)
            if self.heap:
                self.heap.insert(0, self.heap.pop())
                self._down()
            return value
        
        def _up(self):
            index = len(self.heap) - 1
            while index > 0:
                parent_index = (index + 1) // 2 - 1
                if self.heap[parent_index] > self.heap[index]:
                    self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                    index = parent_index
                else: break

        def _down(self):
            index = 0
            child_index = index * 2 + 1
            while child_index < len(self.heap):
                if child_index + 1 < len(self.heap) and self.heap[child_index + 1] < self.heap[child_index]:
                    child_index += 1

                if self.heap[child_index] > self.heap[index]: break
                self.heap[child_index], self.heap[index] = self.heap[index], self.heap[child_index]
                index = child_index
                child_index = index * 2 + 1

    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     heap = Solution.HeapSort(k)
    #     for row in matrix:
    #         for num in row:
    #             heap.add(num)
    #     return heap.get()

    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     ptrs, ans = [0] * len(matrix), 0
    #     while k > 0:
    #         k -= 1
    #         row, temp = 0, float('inf')
    #         for i, j in enumerate(ptrs):
    #             if j >= len(matrix): continue
    #             if matrix[i][j] < temp:
    #                 temp, row = matrix[i][j], i
    #         ans = temp
    #         ptrs[row] += 1
    #     return ans

    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     heap = Solution.HeapSort(k)
    #     for i in range(len(matrix)):
    #         row = matrix[i]
    #         heap.add((row[0], i, 0))
        
    #     while k > 1:
    #         k -= 1
    #         _, i, j = heap.pop()
    #         if j + 1 < len(matrix):
    #             heap.add((matrix[i][j + 1], i, j + 1))
    #     return heap.get()[0]

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        def check(mid: int) -> bool:
            count = 0
            i, j = len(matrix) - 1, 0
            while i >= 0 and j < len(matrix):
                if matrix[i][j] <= mid:
                    count += i + 1
                    j += 1
                elif matrix[i][j] > mid:
                    i -= 1 
            return count < k
        
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid

        return left

if __name__ == '__main__':
    print(Solution().kthSmallest([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
    print(Solution().kthSmallest([[1,2],[1,3]], 1))
    print(Solution().kthSmallest([[1,2],[3,3]], 4))
    print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
    print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 7))
    print(Solution().kthSmallest([[48,65,70,113,133,163,170,216,298,389],[89,169,215,222,250,348,379,426,469,554],[178,202,253,294,367,392,428,434,499,651],[257,276,284,332,380,470,516,561,657,698],[275,331,391,432,500,595,602,673,758,783],[357,365,412,450,556,642,690,752,801,887],[359,451,534,609,654,662,693,766,803,964],[390,484,614,669,684,711,767,804,857,1055],[400,515,683,732,812,834,880,930,1012,1130],[480,538,695,751,864,939,966,1027,1089,1224]], 43))
