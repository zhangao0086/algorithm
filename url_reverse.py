#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:

    def reverse(self, url: list):
        def rotate(left, right):
            for i in range(left, (right + left) // 2):
                url[i], url[right + left - i - 1] = url[right + left - i - 1], url[i]

        url_length, start = len(url), 0
        rotate(0, url_length)
        for i in range(url_length):
            if url[i] == ".":
                rotate(start, i)
                start = i + 1
        if start < url_length:
            rotate(start, url_length)
        return url

if __name__ == '__main__':
    test_cases = [
        "www.toutiao",
        "www.toutiao.cn",
        "www.toutiao.com.cn",
    ]

    # Python 字符串是不可变对象，用字符数组模拟可变字符串
    for case in test_cases:
        print(f"{case} => {''.join(Solution().reverse(list(case)))}")