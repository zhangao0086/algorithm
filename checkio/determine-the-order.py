#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from collections import OrderedDict

def checkio(data):
    data = ["".join(OrderedDict.fromkeys(d)) for d in data]
    letters = sorted(set("".join(data)))
    ans = ""
    while letters:
        for letter in letters:
            if not any(letter in d[1:] for d in data):
                ans += letter
                break
        data = [d.replace(letter, "") for d in data]
        letters.remove(letter)
    return ans

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["llo","low","lino","itttnosw"]) == "litnosw"
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss","aa"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
