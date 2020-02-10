#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"


def insert_sort(nums: [int]) -> [int]:
    if len(nums) < 2:
        return nums

    j = 0
    for i in range(1, len(nums)):
        inserted = nums[i]
        for j in range(i, -1, -1):
            if inserted < nums[j - 1]:
                nums[j] = nums[j - 1]
            else:
                break
        nums[j] = inserted

    return nums


if __name__ == '__main__':
    print(insert_sort([9,1,3,5,-10,2]))