#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List, Tuple

def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    def is_intersect(circle_1, circle_2) -> bool:
        x1, x2, r1 = circle_1
        y1, y2, r2 = circle_2
            
        distance = ((x1 - y1) ** 2 + (x2 - y2) ** 2) ** 0.5
        return distance < r1+r2 and not (distance + r1 <= r2 or distance + r2 <= r1)

    chains = []
    for circle in circles:
        new_chain = [circle]
        others = []
        for chain in chains:
            if any(is_intersect(c, circle) for c in chain):
                new_chain += chain
            else:
                others += [chain]
        chains = [new_chain] + others
    return len(chains)

if __name__ == '__main__':
    assert count_chains([[0,0,2],[1,0,3],[3,0,1],[2,1,1],[-2,-2,1],[0,0,4],[-3,0,1]]) == 3
    assert count_chains([[1,3,1],[2,2,1],[4,2,1],[5,3,1],[3,3,1]]) == 1

    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")