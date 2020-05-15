#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         if word1 == word2: return 0
#         if not word1: return len(word2)
#         if not word2: return len(word1)

#         if word1[0] == word2[0]:
#             return self.minDistance(word1[1:], word2[1:])
#         else:
#             return 1 + min(
#                 self.minDistance(word1[1:], word2[1:]), 
#                 self.minDistance(word1[1:], word2),
#                 self.minDistance(word1, word2[1:]),
#             )

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         cache = {}

#         def dp(word1: str, word2: str) -> int:
#             if word1 == word2: return 0
#             if not word1: return len(word2)
#             if not word2: return len(word1)

#             if (word1, word2) not in cache:
#                 if word1[0] == word2[0]:
#                     cache[(word1, word2)] = dp(word1[1:], word2[1:])
#                 else:
#                     cache[(word1, word2)] = 1 + min(
#                         dp(word1[1:], word2[1:]), 
#                         dp(word1[1:], word2),
#                         dp(word1, word2[1:]),
#                     )
#             return cache[(word1, word2)]
#         return dp(word1, word2)

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         cache = {}
#         def dp(i: int, j: int) -> int:
#             if (i, j) not in cache:
#                 if i >= len(word1): return len(word2) - j
#                 if j >= len(word2): return len(word1) - i

#                 if word1[i] == word2[j]:
#                     cache[(i, j)] = dp(i + 1, j + 1)
#                 else:
#                     cache[(i, j)] = 1 + min(
#                         dp(i + 1, j + 1), 
#                         dp(i + 1, j),
#                         dp(i, j + 1),
#                     )
#             return cache[(i, j)]
#         return dp(0, 0)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         pre, cur = [j for j in range(len(word2) + 1)], [0] * (len(word2) + 1)

#         for i in range(1, len(word1) + 1):
#             cur[0] = i
#             for j in range(1, len(word2) + 1):
#                 if word1[i - 1] == word2[j - 1]:
#                     cur[j] = pre[j - 1]
#                 else:
#                     cur[j] = 1 + min(pre[j - 1], pre[j], cur[j - 1])
#             pre, cur = cur, pre
#         return pre[-1]

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         pre, cur = 0, [j for j in range(len(word2) + 1)]

#         for i in range(1, len(word1) + 1):
#             pre = cur[0]
#             cur[0] = i
#             for j in range(1, len(word2) + 1):
#                 temp = cur[j]
#                 if word1[i - 1] == word2[j - 1]:
#                     cur[j] = pre
#                 else:
#                     cur[j] = 1 + min(pre, cur[j], cur[j - 1])
#                 pre = temp
#         return cur[-1]

if __name__ == '__main__':
    assert Solution().minDistance("sea", "eat") == 2
    assert Solution().minDistance("park", "spake") == 3
    assert Solution().minDistance("horse", "ros") == 3
    assert Solution().minDistance("intention", "execution") == 5
    assert Solution().minDistance("", "") == 0
    assert Solution().minDistance("1", "") == 1
    assert Solution().minDistance("12345", "") == 5
    assert Solution().minDistance("12345", "1245") == 1


    # park => spark
    # spark => spakk
    # spakk => spake