#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:

    # 解法一: x = f(x-1) + f(x-2)
    def climbStairs(self, n: int) -> int:
        if n <= 1: return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    # 解法二: 备忘录
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    # 解法三: 根据前两结果顺序递推
    def climbStairs(self, n: int) -> int:
        pre1, pre2 = 0, 1
        for _ in range(1, n):
            pre1, pre2 = pre2, pre1 + pre2

        return pre1 + pre2

if __name__ == '__main__':
    assert Solution().climbStairs(0) == 1
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5
    assert Solution().climbStairs(5) == 8
    assert Solution().climbStairs(6) == 13
    assert Solution().climbStairs(7) == 21
    assert Solution().climbStairs(8) == 34
    assert Solution().climbStairs(9) == 55
    assert Solution().climbStairs(10) == 89