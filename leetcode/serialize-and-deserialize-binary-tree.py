#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        
        ans = []
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node:
                ans.append(str(node.val))
                stack.append(node.left)
                stack.append(node.right)
            else:
                ans.append("#")

        return " ".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        vals = data.split()

        root = TreeNode(int(vals[0]))
        stack, i = [root], 1
        while i < len(vals):
            parent = stack.pop(0)
            if vals[i] != '#':
                parent.left = TreeNode(int(vals[i]))
                stack.append(parent.left)
            i += 1
            if vals[i] != '#':
                parent.right = TreeNode(int(vals[i]))
                stack.append(parent.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    ans = Codec().serialize(root)
    tree = Codec().deserialize(ans)

    Codec().serialize(None)
    Codec().deserialize(None)