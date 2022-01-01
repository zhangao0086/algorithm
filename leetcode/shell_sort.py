#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"


def shell_sort(nums: [int]) -> [int]:
    length = len(nums)
    gap = int(length / 2)
    j = 0
    while gap > 0:
        for i in range(gap, length):
            inserted = nums[i]
            for j in range(i, -1, -gap):
                if j - gap < 0 or inserted > nums[j - gap]:
                    break
                else:
                    nums[j] = nums[j - gap]
            nums[j] = inserted
        gap = int(gap / 2)

    return nums


if __name__ == '__main__':
    print(shell_sort([123,-2,1,3,0,41,-5]))