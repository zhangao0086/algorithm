#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def decodeString(self, s: str) -> str:
        ans, stack, num = "", [], 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                stack.append((num, ans))
                num, ans = 0, ""
            elif char == "]":
                last_num, last_chars = stack.pop()
                ans = last_chars + last_num * ans
            else:
                ans += char
        return ans

    # def decodeString(self, s: str) -> str:
    #     ans, stack = "", []
    #     i = 0
    #     while i < len(s) and s[i].islower():
    #         ans += s[i]
    #         i += 1

    #     while i < len(s):
    #         j = i
    #         while s[i].isdigit(): i += 1
    #         num = int(s[j:i])

    #         i += 1 # [

    #         j = i
    #         while i < len(s) and s[i].islower(): i += 1
    #         stack.append((num, s[j:i]))
            
    #         while i < len(s) and s[i] == "]":
    #             i += 1
    #             num, chars = stack.pop()
    #             temp = chars * num

    #             while i < len(s) and s[i].islower():
    #                 temp += s[i]
    #                 i += 1

    #             if stack:
    #                 stack[-1] = stack[-1][0], stack[-1][1] + temp
    #             else:
    #                 ans += temp
    #     return ans

if __name__ == '__main__':
    # assert Solution().decodeString("3[a]2[bc]") == "aaabcbc"
    assert Solution().decodeString("3[a2[c]]") == "accaccacc"
    assert Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert Solution().decodeString("abc3[cd]xyz") == "abccdcdcdxyz"