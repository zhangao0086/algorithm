#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # 使用差分数组记录变化
        n = len(s)
        changes = [0] * (n + 1)
        
        # 处理每个shift操作
        for start, end, direction in shifts:
            delta = 1 if direction else -1
            changes[start] += delta
            changes[end + 1] -= delta
        
        # 计算前缀和得到每个位置的最终移动次数
        curr_shift = 0
        result = []
        for i, char in enumerate(s):
            curr_shift = (curr_shift + changes[i]) % 26  # 优化：提前取模
            # 计算新字符：当前字符的ASCII码加上位移量
            new_char = chr((ord(char) - ord('a') + curr_shift) % 26 + ord('a'))
            result.append(new_char)
            
        return ''.join(result)

if __name__ == '__main__':
    assert Solution().shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace"
    # assert Solution().shiftingLetters("dztz", [[0, 0, 0], [1, 1, 1]]) == "catz"