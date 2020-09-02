#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 找出不匹配的括号类型和数量
        left, right = 0, 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                if left == 0: right += 1
                if left > 0: left -= 1
        
        # 找出所有有效的结果
        result = set()
        def match(rem_left: int, rem_right: int, index:int, left_count: int, right_count: int, curr_str: []):
            if index == len(s):
                if rem_left + rem_right == 0:
                    result.add("".join(curr_str))
                return

            char = s[index]
            if char == "(" and rem_left > 0:
                match(rem_left - 1, rem_right, index + 1, left_count, right_count, curr_str)
            elif s[index] == ")" and rem_right > 0:
                match(rem_left, rem_right - 1, index + 1, left_count, right_count, curr_str)
            
            curr_str.append(char)
            if char != "(" and char != ")":
                match(rem_left, rem_right, index + 1, left_count, right_count, curr_str)
            elif char == "(":
                match(rem_left, rem_right, index + 1, left_count + 1, right_count, curr_str)
            elif char == ")" and left_count > right_count:
                match(rem_left, rem_right, index + 1, left_count, right_count + 1, curr_str)
            curr_str.pop()
        match(left, right, 0, 0, 0, [])
        return list(result)

if __name__ == '__main__':
    print(Solution().removeInvalidParentheses("()())()"))
    print(Solution().removeInvalidParentheses("())("))