#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def preorder_traversal(root: TreeNode):
  nodes = []
  pointer = root
  while pointer or nodes:
    if pointer != None:
      print(pointer.value)
      nodes.append(pointer)
      pointer = pointer.left
    else:
      pointer = nodes.pop().right

def levelorder_traversal(root: TreeNode):
  nodes = [root]
  while nodes:
    length = len(nodes)
    while length > 0:
      node = nodes.pop(0)
      print(node.value)
      
      if node.left != None:
        nodes.append(node.left)
      
      if node.right != None:
        nodes.append(node.right)
      
      length -= 1

if __name__ == '__main__':
    root = TreeNode("a")
    root.left = TreeNode("b")
    root.right = TreeNode("c")

    root.left.left = TreeNode("d")
    root.left.right = TreeNode("e")

    preorder_traversal(root)
    print("---")
    levelorder_traversal(root)