#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

def is_balanced(line: str) -> bool:
    if line == '': return True
    replaced_line = line.replace('()', '').replace('[]', '').replace('{}', '')
    if replaced_line == line: return False
    return is_balanced(replaced_line)

def remove_brackets(line: str) -> str:
    if is_balanced(line): return line
    ans = ''
    for i in range(len(line)):
        temp = remove_brackets(line[:i] + line[i+1:])
        if len(temp) > len(ans): ans = temp
    return ans

if __name__ == '__main__':
    print("Example:")
    print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]'
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    assert remove_brackets('[(])') == '()'
    print("Coding complete? Click 'Check' to earn cool rewards!")
