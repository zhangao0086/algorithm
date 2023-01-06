#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Robot:

    __next_direction__ = {
        'North': 'West',
        'West': 'South',
        'South': 'East',
        'East': 'North'
    }

    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.direction = "East"
        self.position = (0, 0)
        self.perimeter = width * 2 + height * 2 - 4

    def step(self, num: int) -> None:
        num %= self.perimeter
        if num == 0: num = self.perimeter

        while num:
            x, y = self.position
            if self.direction == "North":
                y = self.position[1] + num
                overflow = y - (self.height-1)
            elif self.direction == "East":
                x = self.position[0] + num
                overflow = x - (self.width-1)
            elif self.direction == "South":
                y = self.position[1] - num
                overflow = 0 - y
            else: # West
                x = self.position[0] - num
                overflow = 0 - x

            num = 0
            if x < 0 or x > self.width-1 or y < 0 or y > self.height-1:
                self.direction = Robot.__next_direction__[self.direction]
                num = overflow
                x, y = max(0, min(self.width-1, x)), max(0, min(self.height-1, y))
            self.position = x, y

    def getPos(self) -> List[int]:
        return list(self.position)

    def getDir(self) -> str:
        return self.direction

# Your Robot object will be instantiated and called as such:
obj = Robot(6, 3)
obj.step(8)
print(obj.getPos(), obj.getDir())