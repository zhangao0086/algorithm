#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'

        ans = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                temp = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0')) + carry
                carry = (temp + ans[i+j+1]) // 10
                ans[i+j+1] = (temp + ans[i+j+1]) % 10
            ans[i] += carry
        return "".join(map(str, ans)).lstrip('0')

# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
#         first, second = 0, 0
#         for num in num1:
#             first = first * 10 + ord(num) - ord('0')
#         for num in num2:
#             second = second * 10 + ord(num) - ord('0')
#         return str(first * second)

if __name__ == '__main__':
    assert Solution().multiply("2", "3") == "6"
    assert Solution().multiply("123", "456") == "56088"