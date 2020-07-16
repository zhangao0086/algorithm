#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def move(self, n) -> int:
        # return 2 ** n - 1

        # def recursive(n, count) -> int:
        #     if n < 1: return count
        #     if n == 1: return count + 1
        #     count = recursive(n-1, count + 1)
        #     return recursive(n-1, count)
        # return recursive(n, 0)

        def recursive(n, x, y ,z):
            if n < 1: return
            if n == 1: 
                print(f"从{x}移动到{z}")
                return
            recursive(n-1, x, z, y)
            print(f"从{x}移动到{z}")
            recursive(n-1, y, x, z)
        recursive(n, "x", "y", "z")

        # ans = 0
        # for i in range(n):
        #     ans += ans + 1
        # return ans

if __name__ == '__main__':
    print(Solution().move(3))
    print(Solution().move(4))
    print(Solution().move(5))