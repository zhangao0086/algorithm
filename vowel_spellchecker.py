#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    vowel_table = set(['a', 'e', 'i', 'o', 'u'])

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        if len(queries) == 0:
            return []

        def replace_vowel(word: str) -> str:
            return "".join([char if char not in Solution.vowel_table else "a" for char in word])

        hash_table = set(wordlist)
        word_lower_table = {}
        word_vowel_table = {}
        for word in wordlist:
            word_lower = word.lower()
            word_lower_table.setdefault(word_lower, word)
            word_vowel_table.setdefault(replace_vowel(word_lower), word)

        result = [""] * len(queries)
        i = 0
        for query in queries:
            if query in hash_table:  # exactly matches a word
                result[i] = query
            else:
                query_lower = query.lower()
                if query_lower in word_lower_table:  # matches a word up to capitlization
                    result[i] = word_lower_table[query_lower]
                else:
                    query_without_vowel = replace_vowel(query_lower)
                    if query_without_vowel in word_vowel_table:  # matches a word up to vowel errors
                        result[i] = word_vowel_table[query_without_vowel]

            i += 1

        return result

if __name__ == '__main__':
    wordlist = ["KiTe","kite","hare","Hare"]
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

    print(Solution().spellchecker(wordlist, queries))