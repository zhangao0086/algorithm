#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

def bubble_sort(nums: list[int]):
    iterative = 0
    sorted_border = len(nums) - 1
    for _ in range(sorted_border):
        sorted = True  # 如果是有序的，则直接跳过
        for j in range(0, sorted_border):
            iterative += 1
            if nums[j] > nums[j + 1]:
                sorted = False
                sorted_border = j
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if sorted:
            break

    print(iterative)
    print(nums)


if __name__ == '__main__':
    bubble_sort([7,3,123,31,9,0, 124,125,126,-1])