#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:

    # # dp
    # def longestValidParentheses(self, s: str) -> int:
    #     if not s: return 0

    #     dp = [0] * len(s)
    #     for i in range(1, len(s)):
    #         char = s[i]
    #         if char == ')':
    #             if s[i - 1] == '(':
    #                 # 满足条件，至少 + 2，如果'('前还有有效长度，继续加上
    #                 dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
    #             elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
    #                 # 满足条件，符合 (())
    #                 # 如果 (()) 前还有()，继续加上
    #                 dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
    #     return max(dp)

    # # stack
    # def longestValidParentheses(self, s: str) -> int:
    #     stack, max_length = [-1], 0
    #     for i in range(len(s)):
    #         char = s[i]
    #         if char == '(':
    #             stack.append(i)
    #         else:
    #             stack.pop()
    #             if stack:
    #                 # 栈不是空的，括号配对成功，通过栈顶元素计算有效长度
    #                 max_length = max(max_length, i - stack[-1])
    #             else:
    #                 stack.append(i)
    #     return max_length

    # Without extra space
    def longestValidParentheses(self, s: str) -> int:
        def traversal(iterator, reset_checker) -> int:
            left, right, max_length = 0, 0, 0
            for i in iterator:
                char = s[i]
                if char == '(':
                    left += 1
                else:
                    right += 1

                if left == right:
                    # 满足条件，配对成功
                    max_length = max(max_length, left + right)

                if reset_checker(left, right):
                    left, right = 0, 0
            return max_length

        return max(
            # 先从左往右
            traversal(range(len(s)), lambda left, right: right > left),
            # 再从右往左
            traversal(range(len(s)-1, -1, -1), lambda left, right: left > right)
        )

if __name__ == '__main__':
    print(Solution().longestValidParentheses(""))
    print(Solution().longestValidParentheses("()()"))
    print(Solution().longestValidParentheses("(()()"))
    print(Solution().longestValidParentheses("(()"))
    print(Solution().longestValidParentheses("()(()"))
    print(Solution().longestValidParentheses(")()())"))

    print(Solution().longestValidParentheses("()(((())()())))))())))))))))"))

    print(Solution().longestValidParentheses("()"))
    print(Solution().longestValidParentheses(")"))