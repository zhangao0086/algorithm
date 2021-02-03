#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

def checkio(data):
    dp = {}
    for i in range(1, len(data) + 1):
        for j in range(len(data) + 1 - i):
            dp[j, i] = set([int(data[j:j+i])])
            for k in range(1, i):
                dp[j, i] |= set(g for x in dp[j, k] for y in dp[j + k, i - k] for g in ([x + y, x - y, x * y] + [x / y] if y != 0 else []))
        
    return 100 not in dp[0, len(data)]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio('000000') == True, "All zeros"
    assert checkio('707409') == True, "You can not transform it to 100"
    assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
