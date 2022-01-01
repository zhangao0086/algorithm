#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = set([
            'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 
        ])
        ans, words_count, first_char, is_begin = [], 1, "", True
        for char in S:
            if char == " ":
                if is_begin: continue
                tail = "a" * words_count
                ans.append(f"{first_char}ma{tail}")
                is_begin, first_char, words_count = True, "", words_count + 1
            elif is_begin:
                if words_count > 1: ans.append(" ")
                if char in vowel:
                    ans.append(char)
                else:
                    first_char = char
                is_begin = False
            else:
                ans.append(char)
        if not is_begin:
            tail = "a" * words_count
            ans.append(f"{first_char}ma{tail}")
        return "".join(ans)

if __name__ == '__main__':
    assert Solution().toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    assert Solution().toGoatLatin(" I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    assert Solution().toGoatLatin(" I speak Goat Latin ") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    assert Solution().toGoatLatin("The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    