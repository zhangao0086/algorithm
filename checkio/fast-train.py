#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

def fast_train(sections: List[List[int]]) -> int:
    limits = sum(([max_speed] * distance for distance, max_speed in sections), [])
    routes, destination = [[1]], len(limits)
    while routes:
        route = routes.pop(0)
        position, speed = sum(route), route[-1]
        if position == destination and speed == 1:
            return len(route)
        routes += [route + [next_speed] for next_speed in [speed - 1, speed, speed + 1]
            if 0 < next_speed <= destination - position and all(next_speed <= limits[position + i] for i in range(next_speed))
        ]

    assert False, "无解"

if __name__ == '__main__':
    print("Example:")
    print(fast_train([(4, 3)]))

    assert fast_train([(4, 3)]) == 3
    assert fast_train([(9, 10)]) == 5
    assert fast_train([(5, 5), (4, 2)]) == 6
    print("Coding complete? Click 'Check' to earn cool rewards!")
