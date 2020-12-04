#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

import functools, os

def calc(target: int, count: int):
    nums = []
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r+") as file:
            for line in file.readlines():
                nums.append(int(line))
    nums.sort()
    ans = sum_of_count(nums, 0, len(nums)-1, target, count)
    return ans

def sum_of_count(nums: [int], begin: int, end: int, target: int, count: int) -> [int]:
    if count == 2: 
        return search(nums, begin, end, target)
    for i in range(begin, end):
        if nums[i] + sum(ans := sum_of_count(nums, i + 1, end, target - nums[i], count - 1)) == target and len(ans)+1 == count:
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
    print(calc(2020, 2))
    print(calc(2020, 3))
    print(calc(2020, 4))
    print(calc(2020, 5))