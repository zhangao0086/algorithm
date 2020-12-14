#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

import os, re

def valid_count(lines):
    if lines[-1] != "": lines.append("")
    ans, passport = 0, {}
    for line in lines:
        if line == "":
            temp, passport = passport, {}
            if len(temp) == 8 or (len(temp) == 7 and "cid" not in temp):
                if not temp["byr"].isnumeric() or not (1920 <= int(temp["byr"]) <= 2002):
                    continue
                if not temp["iyr"].isnumeric() or not (2010 <= int(temp["iyr"]) <= 2020):
                    continue
                if not temp["eyr"].isnumeric() or not (2020 <= int(temp["eyr"]) <= 2030):
                    continue
                if not ((temp["hgt"].endswith("cm") and 150 <= int(temp["hgt"][:-2]) <= 193) or (temp["hgt"].endswith("in") and 59 <= int(temp["hgt"][:-2]) <= 76)):
                    continue
                if not re.compile("#[0-9a-f]{6}").match(temp["hcl"]):
                    continue
                if not (temp["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]):
                    continue
                if not (len(temp["pid"]) == 9 and temp["pid"].isnumeric()):
                    continue
                ans += 1
        else:
            passport.update({item[:3]:item[4:] for item in line.split(" ")})
    return ans

if __name__ == '__main__':
    input = []
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r+") as file:
        for line in file.readlines():
            input.append(line.strip())
    print(valid_count(input))
