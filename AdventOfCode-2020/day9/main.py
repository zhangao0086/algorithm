#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

import os

def find_wrong(numbers: list[int]) -> int:
    for i in range(25, len(numbers)):
        num, table = numbers[i], set(numbers[i-25:i])
        found = False
        for item in table:
            if num - item in table:
                found = True
                break
        if not found:
            return num

def find_part2(numbers: list[int], target: int) -> int:
    left, right = 0, 1
    while left < len(numbers):
        sublist = numbers[left:right]
        total = sum(sublist)
        if total == target:
            return max(sublist) + min(sublist)
        elif total < target and right < len(numbers):
            right += 1
        else:
             left += 1

if __name__ == '__main__':
    input = []
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r+") as file:
        for line in file.readlines():
            input.append(int(line.strip()))
    part1 = find_wrong(input)
    print(part1)

    part2 = find_part2(input, part1)
    print(part2)