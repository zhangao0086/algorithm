#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

import os

def n_sum(nums: [int], begin: int, end: int, target: int, n: int) -> [int]:
    if n == 2: 
        return search(nums, begin, end, target)
    for i in range(begin, end):
        if nums[i] + sum(ans := n_sum(nums, i + 1, end, target - nums[i], n - 1)) == target and len(ans)+1 == n:
            return [nums[i]] + ans
    return []

def search(nums: [int], begin: int, end: int, target: int) -> [int, int]:
    while begin < end:
        sum = nums[begin] + nums[end]
        if sum == target:
            break
        elif sum < target:
            begin += 1
        else:
            end -= 1
    if (num1 := nums[begin]) + (num2 := nums[end]) == target:
        return [num1, num2]
    return []

if __name__ == '__main__':
    nums = []
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
            for line in file.readlines():
                nums.append(int(line))
    nums.sort()

    print(n_sum(nums, 0, len(nums)-1, 2020, 2))
    print(n_sum(nums, 0, len(nums)-1, 2020, 3))
    print(n_sum(nums, 0, len(nums)-1, 2020, 4))
    print(n_sum(nums, 0, len(nums)-1, 2020, 5))
