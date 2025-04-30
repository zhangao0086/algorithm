#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def count_digits(num):
            if num == 0:
                return 1
            count = 0
            while num > 0:
                count += 1
                num //= 10
            return count
            
        return sum(1 for num in nums if count_digits(num) % 2 == 0)

if __name__ == '__main__':
    solution = Solution()
    print(solution.findNumbers([12,345,2,6,7896]))
    print(solution.findNumbers([555,901,482,1771]))