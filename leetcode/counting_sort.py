#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

def counting_sort(nums: [int]) -> [int]:
    min = nums[0]
    max = nums[0]

    for num in nums:
        if num < min:
            min = num
        elif num > max:
            max = num

    counting_array = [0] * (max - min + 1)
    for num in nums:
        counting_array[num - min] += 1

    result = [0] * len(nums)
    
    index = 0
    for i in range(len(counting_array)):
        for num in range(counting_array[i]):
            result[index] = min + i
            index += 1

    # 变形，记录位置
    # for i in range(1, len(counting_array)):
    #     counting_array[i] += counting_array[i - 1]
    # 
    # for num in nums:
    #     location = counting_array[num - min]
    #     result[location - 1] = num
    #     counting_array[num - min] -= 1
        
    return result

if __name__ == '__main__':
    print(counting_sort([5,3,7,4,8,1,9,10]))