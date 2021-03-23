#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from collections import Counter, defaultdict

class Solution:
    # def minWindow(self, s: str, t: str) -> str:
    #     count = Counter(t)
    #     curr_count, curr_window = defaultdict(list), []
    #     ans = None
    #     for i, char in enumerate(s):
    #         if char in count:
    #             curr_count[char].append(i)
    #             curr_window.append(i)
    #             if len(curr_count[char]) > count[char]:
    #                 curr_window.remove(curr_count[char].pop(0))
    #             if len(curr_window) == len(t) and (not ans or curr_window[-1] - curr_window[0] < ans[1] - ans[0]):
    #                 ans = curr_window[0], i
    #     return "" if not ans else s[ans[0]: ans[1] + 1]

    def minWindow(self, s: str, t: str) -> str:
        count, remaining = Counter(t), len(t)
        l, ans = 0, None
        for r, char in enumerate(s):
            if char in count:
                count[char] -= 1
                if count[char] >= 0:
                    remaining -= 1
                while remaining == 0:
                    curr_len = r - l + 1
                    if not ans or curr_len < ans[1]:
                        ans = l, curr_len

                    l_char = s[l]
                    if l_char in count:
                        count[l_char] += 1
                        if count[l_char] > 0:
                            remaining += 1
                    l += 1
        return "" if not ans else s[ans[0]: ans[0] + ans[1]]

if __name__ == '__main__':
    assert Solution().minWindow("abc", "b") == "b"
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert Solution().minWindow("a", "a") == "a"
    assert Solution().minWindow("A", "a") == ""
    assert Solution().minWindow("abbc", "abc") == "abbc"