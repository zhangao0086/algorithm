#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"


def cocktail_sort(nums: [int]):
    iterative = 0
    for i in range(int(len(nums) / 2)):
        sorted = True
        for j in range(i, len(nums) - 1 - i):
            iterative += 1
            if nums[j] > nums[j + 1]:
                sorted = False
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if sorted:
            break

        for j in range(len(nums) - 2 - i, i, -1):
            iterative += 1
            if nums[j] < nums[j - 1]:
                sorted = False
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

        if sorted:
            break

    print(iterative)
    print(nums)


if __name__ == '__main__':
    cocktail_sort([7,3,123,31,9,0, 124,125,126,-1])