#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root: TreeNode):
    curr: TreeNode = root
    prev: TreeNode = None
    while curr:
        if curr.left is None:
            print(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
            
            if prev.right is None:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                print(curr.val)
                curr = curr.right

if __name__ == '__main__':
    root = TreeNode(2, TreeNode(1, TreeNode(0), TreeNode(-1)), TreeNode(4, TreeNode(3)))
    inorder(root)