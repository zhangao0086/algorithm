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
    elif pattern[0] == '[':
        index = pattern.find(']')
        chars = pattern[1:index]
        pattern = pattern[index+1:]
        
        if chars and ((chars[0] == '!' and first not in chars) or (chars[0] != '!' and first in chars)):
            return unix_match(filename[1:], pattern)
    return False

if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match("nametxt","name[]txt") == False
    assert unix_match("name.txt","name[]txt") == False

    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
