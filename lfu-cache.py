#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from collections import defaultdict

class Node:
    """
    双向链表的节点抽象
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.frequency = 1
        self.previous = self.next = None

class LinkedList:
    """
    双向链表，用于记录同一个频率下的所有节点
    """

    def __init__(self):
        self.dummy = Node(None, None)
        self.dummy.next = self.dummy.previous = self.dummy
        self.size = 0

    def __len__(self):
        return self.size
    
    def push(self, node):
        node.next = self.dummy.next
        node.previous = self.dummy
        node.next.previous = node
        self.dummy.next = node
        self.size += 1

    def pop(self, node = None):
        if self.size == 0: return None

        if node is None:
            node = self.dummy.previous

        node.previous.next = node.next
        node.next.previous = node.previous
        self.size -= 1

        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = self.min_frequency = 0
        self.nodes = {}

        self.linkedLists = defaultdict(LinkedList)

    def get(self, key: int) -> int:
        if key not in self.nodes: return -1

        node = self.nodes.get(key)
        self._update(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return None
        node = self.nodes.get(key)

        if node is None:
            if self.size == self.capacity:
                node = self.linkedLists[self.min_frequency].pop()
                del self.nodes[node.key]
                self.size -= 1

            node = Node(key, value)
            self.nodes[key] = node
            self.size += 1
            self.min_frequency = 1
            self.linkedLists[1].push(node)
        else:
            self._update(node)
            node.value = value
    
    def _update(self, node):
        linkedList = self.linkedLists[node.frequency]
        linkedList.pop(node)

        if self.min_frequency == node.frequency and not self.linkedLists[self.min_frequency]:
            self.min_frequency += 1
        
        node.frequency += 1
        self.linkedLists[node.frequency].push(node)

# Your LFUCache object will be instantiated and called as such:
if __name__ == '__main__':
    lfu = LFUCache(0)
    lfu.put(0, 0)
    lfu.get(0)

    lfu = LFUCache(2)
    lfu.put(1, 1)   # cache=[1,_], cnt(1)=1
    lfu.put(2, 2)   # cache=[2,1], cnt(2)=1, cnt(1)=1
    assert lfu.get(1) == 1
                    # cache=[1,2], cnt(2)=1, cnt(1)=2
    lfu.put(3, 3)   # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                    # cache=[3,1], cnt(3)=1, cnt(1)=2
    assert lfu.get(2) == -1
    assert lfu.get(3) == 3
                    # cache=[3,1], cnt(3)=2, cnt(1)=2
    lfu.put(4, 4)   # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                    # cache=[4,3], cnt(4)=1, cnt(3)=2
    assert lfu.get(1) == -1
    assert lfu.get(3) == 3
                    # cache=[3,4], cnt(4)=1, cnt(3)=3
    assert lfu.get(4) == 4