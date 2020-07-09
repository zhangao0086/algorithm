#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

import math

def _sum(n: int) -> int:
    dp = [[[]]] + [[] for _ in range(n)]
    max_num = int(n**0.5)
    for i in range(1, max_num + 1):
        num = i * i
        for index in range(num, n + 1):
            position = index - num
            dp[index] += [collection + [num] for collection in dp[position]]
    return max(dp[-1])
    # return len(max(dp[-1]))

def _sum2(n: int) -> int:
    def _recursive(num: int) -> []:
        if num == 0: return []
        if num == 1: return [1]
        root = int(num**0.5)
        return [root * root] + _recursive(num - root * root)
    return _recursive(n)
    # return len(_recursive(n))

def _sum3(n: int) -> int:
    square_numbers = set([num * num for num in range(1, int(n**0.5) + 1)])
    def _recursive(num: int) -> int:
        if num in square_numbers: return 1
        ans = float('inf')
        for square in square_numbers:
            if num < square: continue
            ans = min(_recursive(num - square) + 1, ans)
        return ans
    return _recursive(n)

def _sum4(n: int) -> int:
    square_numbers = [num * num for num in range(1, int(n**0.5) + 1)]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(n+1):
        for square in square_numbers:
            if i < square: break
            dp[i] = min(dp[i-square]+1, dp[i])

    return dp[-1]

def _sum4(n: int) -> int:
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(n+1):
        for j in range(1, int(i**0.5)+1):
            dp[i] = min(dp[i-j*j]+1, dp[i])

    return dp[-1]

def _sum5(n: int) -> int:
    stack, max_root, ans = set([n]), int(n**0.5), 0
    while stack:
        ans, next_stack = ans + 1, set()
        for num in stack:
            for root in range(1, max_root + 1):
                square = root * root
                if num == square: return ans
                elif square > num: break
                else: next_stack.add(num - square)

        stack = next_stack
    return ans

if __name__ == '__main__':
    # print(_sum2(5))
    # print(_sum2(12))
    # print(_sum2(27))
    # print(_sum2(16))
    # print(_sum2(9))
    # print(_sum2(15))
    # print(_sum2(2595321))
    
    # print(_sum3(43))
    # print(_sum3(5))
    # print(_sum3(9))
    # print(_sum3(12))
    # print(_sum3(15))
    # print(_sum3(16))
    # print(_sum3(27))
    # print(_sum3(2595321))

    # print(_sum4(43))
    # print(_sum4(5))
    # print(_sum4(9))
    # print(_sum4(12))
    # print(_sum4(15))
    # print(_sum4(16))
    # print(_sum4(27))
    # print(_sum4(2595321))

    # print(_sum5(43))
    # print(_sum5(5))
    # print(_sum5(9))
    # print(_sum5(12))
    # print(_sum5(15))
    # print(_sum5(16))
    # print(_sum5(27))
    print(_sum5(2595320))
    print(_sum5(2595321))