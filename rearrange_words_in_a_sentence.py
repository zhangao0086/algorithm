#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    
    # 基于 right-most 的二分
    # def arrangeWords(self, text: str) -> str:
    #     ans = []

    #     def right_most(target: int) -> int:
    #         left, right = 0, len(ans)
    #         while left < right:
    #             middle = (left + right) // 2
    #             if len(ans[middle]) > target:
    #                 right = middle
    #             else:
    #                 left = middle + 1
    #         return left

    #     start, end = 0, 0
    #     while end <= len(text):
    #         if end == len(text) or text[end] == " ":
    #             word = text[start:end]
    #             index = right_most(len(word))
    #             if index == len(ans):
    #                 ans.append(word)
    #             else:
    #                 ans.insert(index, word)
    #             start = end + 1
    #         end += 1
    #     return " ".join(ans).capitalize()

    # 基于归并排序
    def arrangeWords(self, text: str) -> str:
        def merge_sort(words:[]) -> []:
            half = len(words) // 2
            if half:
                left, right = merge_sort(words[:half]), merge_sort(words[half:])
                for i in range(len(words)):
                    if not right or (left and len(left[0]) <= len(right[0])):
                        words[i] = left.pop(0)
                    else:
                        words[i] = right.pop(0)
            return words
        
        ans = text.split(" ")
        ans[0] = ans[0].lower()
        merge_sort(ans)
        ans[0] = ans[0].capitalize()
        return " ".join(ans)

if __name__ == '__main__':
    assert Solution().arrangeWords("Keep calm") == "Keep calm"
    assert Solution().arrangeWords("Keep calm and code on") == "On and keep calm code"
    assert Solution().arrangeWords("Leetcode is cool") == "Is cool leetcode"