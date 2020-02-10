#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

def heap_sort(nums: [int]):
    # 堆化，从最后一个非叶子节点开始
    for index in range(int((len(nums) - 2) / 2), 0, -1):
        down_adjust(nums, index, len(nums))
    print(nums)
    
    length = len(nums)
    while length > 1:
        down_adjust(nums, 0, length)
        nums[0], nums[length - 1] = nums[length - 1], nums[0]
        length -= 1
    print(nums)


# 构建大顶堆，将元素下沉
def down_adjust(nums: [int], parent_index: int, length: int):
    temp = nums[parent_index]
    child_index = parent_index * 2 + 1
    while child_index < length:
        if child_index + 1 < length and nums[child_index + 1] > nums[child_index]:
            child_index += 1

        if temp > nums[child_index]:
            break

        nums[parent_index] = nums[child_index]
        parent_index = child_index
        child_index = child_index * 2 + 1
    nums[parent_index] = temp


if __name__ == '__main__':
    heap_sort([4,12,6,9,0,-1,23,1,7])
    