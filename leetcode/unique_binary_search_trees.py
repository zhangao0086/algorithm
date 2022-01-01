#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n+1)
        G[0] = G[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
        return G[-1]

if __name__ == '__main__':
    assert Solution().numTrees(3) == 5
    assert Solution().numTrees(1) == 1