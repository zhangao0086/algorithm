#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        cache = {}
        
        def dfs(old):
            if not old: return None

            node = cache.get(old, Node(old.val))
            if old not in cache:
                cache[old] = node
                node.next = dfs(old.next)
                node.random = dfs(old.random)
            return node
        return dfs(head)

if __name__ == '__main__':
    node1 = Node(7)

    node2 = Node(1)
    node2.random = node1
    node1.random = node2
    node1.next = node2

    new = Solution().copyRandomList(node1)
    print(new)
    
    node1 = Node(7)

    node2 = Node(13)
    node2.random = node1
    node1.next = node2

    node3 = Node(11)
    node2.next = node3

    node4 = Node(10)
    node4.random = node3
    node3.next = node4

    node5 = Node(1)
    node5.random = node1
    node3.random = node5
    node4.next = node5

    new = Solution().copyRandomList(node1)
    print(new)

    node1 = Node(1)

    node2 = Node(2)
    node2.random = node2
    node1.next = node2

    new = Solution().copyRandomList(node1)
    print(new)