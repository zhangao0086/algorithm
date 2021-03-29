#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List
from collections import defaultdict

def cheapest_flight(costs: List, a: str, b: str) -> int:
    graph = defaultdict(dict)
    for city1, city2, cost in costs:
        graph[city1][city2] = cost
        graph[city2][city1] = cost

    prices = {city: float('inf') for city in graph}
    prices[a] = 0
    queue = list(graph.keys())
    while queue:
        city = min(queue, key=lambda city: prices[city])
        for dest, cost in graph[city].items():
            prices[dest] = min(prices[dest], prices[city] + cost)
        queue.remove(city)
    return 0 if prices[b] == float('inf') else prices[b]

if __name__ == '__main__':
    print("Example:")
    print(cheapest_flight([ ['A', 'C', 100],
                            ['A', 'B', 20],
                            ['B', 'C', 50]],
        'A',
        'C'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C') == 70
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'C',
 'A') == 70

    assert cheapest_flight([['A', 'C', 40],
  ['A', 'B', 20],
  ['A', 'D', 20],
  ['B', 'C', 50],
  ['D', 'C', 70]],
 'D',
 'C') == 60

    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['D', 'F', 900]],
 'A',
 'F') == 0

    assert cheapest_flight([['A', 'B', 10],
  ['A', 'C', 15],
  ['B', 'D', 15],
  ['C', 'D', 10]],
 'A',
 'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")
