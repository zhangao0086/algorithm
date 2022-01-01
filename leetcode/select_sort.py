#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

def select_sort(nums: [int]):
    for i in range(len(nums)):
        min = i
        for j in range(i, len(nums)):
            if nums[min] > nums[j]:
                min = j

        if i != min:
            nums[i], nums[min] = nums[min], nums[i]
    print(nums)

if __name__ == '__main__':
    select_sort([7,5,1,-19,9,100,3])