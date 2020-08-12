#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.reverse_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.reverse_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.reverse_stack:
            while self.stack:
                self.reverse_stack.append(self.stack.pop())
        
        return self.reverse_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self.stack or self.reverse_stack)

if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    assert obj.peek() == 1
    assert obj.pop() == 1
    assert obj.empty() == False