#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import Iterable

def can_balance(weights: Iterable) -> int:
    if len(weights) == 1: return 0

    for i in range(1, len(weights)):
        left = weights[i-1::-1]
        right = weights[i+1:]

        total_left = sum([i * (times + 1) for times, i in enumerate(left)])
        total_right = sum([i * (times + 1) for times, i in enumerate(right)])

        if total_left == total_right:
            return i

    return -1

    # left, right = 0, len(weights) - 1
    # total_left, total_right = weights[0], weights[right]
    # while left + 2 < right:
    #     if total_left < total_right:
    #         left += 1
    #         total_left = sum([weights[i] * (times + 1) for times, i in enumerate(range(left, -1, -1))])
    #     else:
    #         right -= 1
    #         total_right = sum([weights[i] * (times + 1) for times, i in enumerate(range(right, len(weights)))])
    
    # return left + 1 if total_left == total_right else -1

if __name__ == '__main__':
    print("Example:")
    print(can_balance([6, 1, 10, 5, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert can_balance([6, 1, 10, 5, 4]) == 2
    assert can_balance([10, 3, 3, 2, 1]) == 1
    assert can_balance([7, 3, 4, 2, 9, 7, 4]) == -1
    assert can_balance([42]) == 0
    assert can_balance([1,1,1,9,1,1,1]) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
