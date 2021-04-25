#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# def can_pass(matrix, first, second, pathes = []):
#     if first == second: return True

#     i, j = first[0], first[1]
#     for i_offset, j_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         new_i, new_j = i + i_offset, j + j_offset
#         if not (0 <= new_i < len(matrix)): continue
#         if not (0 <= new_j < len(matrix[0])): continue
#         if matrix[new_i][new_j] != matrix[first[0]][first[1]]: continue
#         if (new_i, new_j) in pathes: continue

#         if can_pass(matrix, (new_i, new_j), second, pathes + [first]):
#             return True

#     return False

from collections import defaultdict

def can_pass(matrix, first, second, pathes = []):
    to_check, visited = [first], defaultdict(set), 

    while to_check:
        i, j = to_check.pop()
        if (i, j) == second: return True
        if j in visited[i]: continue
        visited[i].add(j)

        for i_offset, j_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = i + i_offset, j + j_offset
            if not (0 <= new_i < len(matrix)): continue
            if not (0 <= new_j < len(matrix[0])): continue
            if matrix[new_i][new_j] != matrix[first[0]][first[1]]: continue
            if (new_i, new_j) in pathes: continue

            to_check.append((new_i, new_j))

    return False

if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
