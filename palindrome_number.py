#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False

    #     reverse_number = 0
    #     temp = x
    #     while temp != 0:
    #         reverse_number = reverse_number * 10 + temp % 10
    #         temp //= 10

    #     return x == reverse_number
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0:
            return False

        reverse_number = 0
        while x > reverse_number:
            reverse_number = reverse_number * 10 + x % 10
            x //= 10

        return x == reverse_number or x == reverse_number // 10

if __name__ == '__main__':
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(-121))
    print(Solution().isPalindrome(10))
    print(Solution().isPalindrome(1001))
    print(Solution().isPalindrome(10101))