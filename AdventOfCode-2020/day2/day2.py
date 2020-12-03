#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

import os

# def is_valid(password: str) -> bool:
#     rule, letter, text = password.split(" ")
#     letter = letter[0]
#     lowest, highest = rule.split("-")

#     count = text.count(letter)
#     return int(lowest) <= count <= int(highest)

def is_valid(password: str) -> bool:
    rule, letter, text = password.split(" ")
    letter = letter[0]
    lowest, highest = rule.split("-")
    lowest, highest = text[int(lowest)-1], text[int(highest)-1]

    return (lowest == letter) ^ (highest == letter)

def check():
    ans = 0
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r+") as file:
        for line in file.readlines():
            if is_valid(line.strip()): ans += 1
    print(ans)

if __name__ == '__main__':
    check()