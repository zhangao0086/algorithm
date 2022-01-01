#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

def merge_sort(nums: [int], temp: [int], start: int, end: int):
    if start >= end:
        return

    middle = int(start + (end - start) / 2)

    merge_sort(nums, temp, start, middle)
    merge_sort(nums, temp, middle + 1, end)

    merge(nums, temp, start, middle, end)

def merge(nums: [int], temp: [int], start: int, middle: int, end: int):
    temp[start:end + 1] = nums[start:end + 1]

    left = start
    right = middle + 1
    
    k = start
    while left <= middle and right <= end:
        if temp[left] < temp[right]:
            nums[k] = temp[left]
            left += 1
        else:
            nums[k] = temp[right]
            right += 1
        k += 1
    
    while left <= middle:
        nums[k] = temp[left]
        k+=1
        left += 1
    
    while right <= end:
        nums[k] = temp[right]
        k+=1
        right += 1

if __name__ == '__main__':
    nums = [45,-4,45,7,23,-13,1,1]
    temp = [None] * len(nums)
    merge_sort(nums, temp, 0, len(nums) - 1)
    print(nums)