#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "xifan"

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = blocks[:k].count('W')
        min_recolors = whites

        for i in range(k, len(blocks)):
            whites += (blocks[i] == 'W') - (blocks[i - k] == 'W')
            min_recolors = min(min_recolors, whites)

        return min_recolors

if __name__ == '__main__':
    assert Solution().minimumRecolors("WBBWWBBWBW", 7) == 3
    assert Solution().minimumRecolors("WBWBBBW", 2) == 0
    assert Solution().minimumRecolors("BWBW", 2) == 1
    assert Solution().minimumRecolors("BWWWBB", 6) == 3