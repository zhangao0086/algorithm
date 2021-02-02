#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List
from collections import Counter, defaultdict

# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         n, m = len(words), len(words[0])
#         ans, window = [], n * m
#         counts = Counter(words)

#         for i in range(len(s) - window + 1):
#             j, seen = 0, defaultdict(int)
#             while j < n:
#                 word = s[i+j*m:i+j*m+m]
#                 if word in counts and counts[word] > seen[word]:
#                     seen[word] += 1
#                     j += 1
#                 else:
#                     break
#             if j == n: ans.append(i)
#         return ans

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, m = len(words), len(words[0])
        ans, window = [], n * m
        counts = Counter(words)

        for k in range(m):
            i = k
            while i < len(s) - window + 1:
                j, seen = 0, defaultdict(int)
                while j < n:
                    word = s[i+window-(j+1)*m:i+window-j*m]
                    if word in counts and counts[word] > seen[word]:
                        seen[word] += 1
                        j += 1
                    else:
                        break
                if j == n: ans.append(i)
                i += max(n - j, 1) * m
                
        return ans

if __name__ == '__main__':
    print(Solution().findSubstring("aaa", ["a","a"]))
    print(Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))
    print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))
    print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
    print(Solution().findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
