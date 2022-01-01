#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:

    def find(self, str1: str, str2: str) -> int:
        dp = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]
        res = 0
        for i in range(1, len(str2)+1):
            for j in range(1, len(str1)+1):
                if str1[j-1] == str2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # 以下为连续的子串解法
                # 以下为不连续的子序列解法
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                res = max(res, dp[i][j]) # res 在子序列下不需要，因为子序列不连续，直接取 dp 最后一个结果即可
        return res

if __name__ == '__main__':
    print(Solution().find("helloworld", "1e2elt3ylu4uol5"))