#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"


# 递归
def quick_sort(nums: [int], low: int, high: int):
    if low > high:
        return

    middle = partition2(nums, low, high)
    quick_sort(nums, low, middle - 1)
    quick_sort(nums, middle + 1, high)

# 栈，非递归
def quick_sort2(nums: [int], low: int, high: int):
    if low >= high:
        return

    stack = [(low, high)]
    while len(stack) > 0:
        left, right = stack.pop(0)

        index = partition2(nums, left, right)

        if left < index - 1:
            stack.append((left, index - 1))

        if right > index + 1:
            stack.append((index + 1, right))

# 大量的内存
def quick_sort3(nums: [int]):
    less = []
    pivot_list = []
    more = []

    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot_list.append(i)
        less = quick_sort3(less)
        more = quick_sort3(more)
        return less + pivot_list + more

# 挖坑法
def partition(nums: [int], low: int, high: int) -> int:
    pivot = nums[low]
    mark = low
    for i in range(mark + 1, high + 1):
        if nums[i] < pivot:
            mark += 1
            nums[i], nums[mark] = nums[mark], nums[i]

    nums[low], nums[mark] = nums[mark], pivot
    return mark


# 指针交换法
def partition2(nums: [int], low: int, high: int) -> int:
    pivot_index = low
    pivot = nums[pivot_index]
    
    while low < high:
        while low < high and nums[high] > pivot:
            high -= 1

        while low < high and nums[low] <= pivot:
            low += 1

        if low < high:
            nums[low], nums[high] = nums[high], nums[low]
    
    nums[pivot_index] = nums[low]
    nums[low] = pivot
    return low


if __name__ == '__main__':
    nums = [120, 100, 105, 103, 118]
    # nums = [-2,11,5,6,100,7,21,46,7,4]
    # quick_sort(nums, 0, len(nums) - 1)
    print(quick_sort3(nums))
    print(nums)
