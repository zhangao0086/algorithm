#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"


class PriorityQueue:

    def __init__(self):
        self.items = []

    def enqueue(self, priority: int):
        self.items.append(priority)
        self._up_adjust()
        print(self.items)

    def dequeue(self):
        self.items[0] = self.items[-1]
        self.items.pop()

        self._down_adjust()
        print(self.items)

    def resize(self):
        pass

    def _up_adjust(self):
        child_index = len(self.items) - 1
        temp = self.items[child_index]
        parent_index = int((child_index - 1) / 2)
        while child_index > 0 and self.items[parent_index] < temp:
            self.items[child_index] = self.items[parent_index]
            child_index = parent_index
            parent_index = int((parent_index - 1) / 2)

        self.items[child_index] = temp

    def _down_adjust(self):
        parent_index = 0
        temp = self.items[parent_index]
        child_index = parent_index * 2 + 1
        length = len(self.items)
        while child_index < length:
            if child_index + 1 < length and self.items[child_index] < self.items[child_index + 1]:
                child_index += 1

            if self.items[child_index] < temp:
                break

            self.items[parent_index] = self.items[child_index]
            parent_index = child_index
            child_index = parent_index * 2 + 1
        self.items[parent_index] = temp


if __name__ == '__main__':
    queue = PriorityQueue()
    queue.enqueue(7)
    queue.enqueue(14)
    queue.enqueue(3)
    queue.enqueue(0)
    queue.enqueue(2)

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    queue.enqueue(-1)
    queue.enqueue(1)
    queue.enqueue(10)