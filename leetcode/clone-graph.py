#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self._clone(node, {})
        
    def _clone(self, node: 'Node', map: dict) -> 'Node':
        if not node: return node

        if node.val in map: return map[node.val]
        
        new_node = Node(node.val)
        map[node.val] = new_node
        for neighbor in node.neighbors:
            new_node.neighbors.append(self._clone(neighbor, map))
        return new_node

if __name__ == '__main__':
    node = Node(1)
    new_node = Solution().cloneGraph(node)
    print(new_node)