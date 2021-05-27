#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

import os
from typing import List

def get_seat_id(seat: str):
    low, high = 0, 127
    left, right = 0, 7

    for row in seat[0:7]:
        if row == 'F':
            high = (low + high) // 2
        else:
            low = (low + high + 1) // 2

    for column in seat[-3:]:
        if column == 'L':
            right = (left + right) // 2
        else:
            left = (left + right + 1) // 2
    
    return low * 8 + left

def get_highest_seat(seats: List[str]):
    seat_ids = []
    for seat in seats:
        seat_ids.append(get_seat_id(seat))
    
    # 返回最大的座位号
    # return max(seat_ids)

    # 返回缺失的座位号
    seat_ids = sorted(seat_ids)
    for i in range(1, len(seat_ids)):
        if seat_ids[i] != seat_ids[i-1] + 1:
            return seat_ids[i] - 1
    
    assert False

if __name__ == '__main__':
    input = []
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r+") as file:
        for line in file.readlines():
            input.append(line.strip())
    print(get_highest_seat(input))