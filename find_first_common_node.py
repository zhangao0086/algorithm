#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Node:
    def __init__(self, x):
        self.value = x
        self.next = None

def find_first_common_node(a: Node, b: Node) -> Node:
  if a == None or b == None:
    return None
  
  map = set()
  while a != None:
    map.add(a)
    a = a.next
  
  while b != None:
    if b in map:
      return b
    else:
      b = b.next
  
  return None

# 不用 map，空间复杂度为常量
def find_first_common_node2(a: Node, b: Node) -> Node:
  if a == None or b == None:
    return None
  
  pointer_a, pointer_b = a, b
  while pointer_a != pointer_b:
    pointer_a = b if pointer_a is None else pointer_a.next
    pointer_b = a if pointer_b is None else pointer_b.next
  
  return pointer_a

if __name__ == '__main__':
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)
    a.next.next.next.next = Node(5)

    b = Node(6)
    b.next = Node(7)
    b.next.next = Node(8)
    b.next.next = a.next.next.next
    # b.next.next.next = a.next.next.next
    b.next.next.next = Node(9)
    
    result = find_first_common_node2(a, b)
    if result:
      print(f"找到公共 Node: {result}, value: {result.value}")
    else:
      print("没有公共 Node")