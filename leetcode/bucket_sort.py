#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

def bucket_sort(nums: [int]) -> [int]:
    if len(nums) < 2:
        return nums
    
    min = max = nums[0]
    for num in nums:
        if num < min:
            min = num
        
        if num > max:
            max = num
    diff = max - min

    buckets = [[] for i in range(len(nums))]
    
    for num in nums:
        bucket_num = int((num - min) / diff * (len(buckets) - 1))
        buckets[bucket_num].append(num)
    
    def quick_sort(nums: [int]):
        def partition(nums: [int], start: int, end: int) -> int:
            pivot, mark = nums[start], start

            for i in range(mark + 1, end + 1):
                if nums[i] < pivot:
                    mark += 1
                    nums[mark], nums[i] = nums[i], nums[mark]
            
            nums[mark], nums[start] = pivot, nums[mark]
            return mark

        if len(nums) <= 1:
            return
        
        stack = [(0, len(nums) - 1)]
        while stack:
            start, end = stack.pop()

            middle = partition(nums, start, end)

            if middle - start > 1:
                stack.append((start, middle - 1))
            
            if end - middle > 1:
                stack.append((middle + 1, end))

    for bucket in buckets:
        quick_sort(bucket)
    
    sorted = [num for bucket in buckets for num in bucket]
    
    return sorted

if __name__ == '__main__':
    print(bucket_sort([7,1.8,1.99,3,5,1,4,6,2,1.9,2.4,2.1,2.3]))