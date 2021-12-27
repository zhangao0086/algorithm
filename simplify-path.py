#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for item in path.split("/"):
            if item == "..":
                if stack:
                    stack.pop()
            elif item and item != ".":
                stack.append(item)
        return "/" + "/".join(stack)

if __name__ == '__main__':
    assert Solution().simplifyPath("/home/") == "/home"
    assert Solution().simplifyPath("/../") == "/"
    assert Solution().simplifyPath("/home//foo/") == "/home/foo"