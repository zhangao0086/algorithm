#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while pushed or popped:
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
            if pushed:
                stack.append(pushed.pop(0))
            else:
                break
        return not stack

if __name__ == '__main__':
    assert Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1])
    assert not Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2])