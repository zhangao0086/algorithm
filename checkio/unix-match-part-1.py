#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

def unix_match(filename: str, pattern: str) -> bool:
    if not filename and not pattern: return True
    if not filename or not pattern: return False
    
    first = filename[0]
    if pattern[0] == '*':
        return any([
            unix_match(filename[1:], pattern),
            unix_match(filename[1:], pattern[1:]),
        ])
    elif pattern[0] == '?' or pattern[0] == first:
        return unix_match(filename[1:], pattern[1:])
    else:
        return False

if __name__ == '__main__':
    print("Example:")
    # print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    # assert unix_match('somefile.txt', '*') == True
    # assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
