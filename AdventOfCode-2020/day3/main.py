#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

import os

def solution(i_step: int, j_step: int):
    map = []
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r+") as file:
        for line in file.readlines():
            map.append(line.strip())
    ans = 0
    i, j = 0, 0
    while j < len(map):
        line = map[j]
        if line[i % len(line)] == "#":
            ans += 1
        j += j_step
        i += i_step
    print(ans)

if __name__ == '__main__':
    solution(1, 1)
    solution(3, 1)
    solution(5, 1)
    solution(7, 1)
    solution(1, 2)