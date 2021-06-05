#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

def chess_knight(start, moves):
    ans = set()
    stack = [((ord(start[0]), int(start[1])), moves)]
    while stack:
        (column, row), moves = stack.pop(0)
        for i, j in [(-2, -1), (-2, 1), (2, 1), (2, -1)]:
            for possible_column, possible_row in [
                (column + i, row + j),
                (column + j, row + i),
            ]:
                if ord('h') >= possible_column >= ord('a') and 0 < possible_row <= 8:
                    cell = (possible_column, possible_row)
                    if cell not in ans:
                        ans.add(cell)
                        if moves > 1: stack.append((cell, moves - 1))
    return sorted([chr(x)+str(y) for (x, y) in ans])

if __name__ == '__main__':
    print("Example:")
    print(chess_knight('a1', 1))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight('a1', 1) == ['b3', 'c2']
    assert chess_knight('h8', 2) == ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']
    print("Coding complete? Click 'Check' to earn cool rewards!")