#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from sum_root_to_leaf_numbers import TreeNode

# class Solution:

#     def tree2str(self, t: TreeNode) -> str:
#         if t is None:
#             return ''

#         if t.right:
#             return "%s(%s)(%s)" % (t.val, self.tree2str(t.left), self.tree2str(t.right))
#         elif t.left:
#             return "%s(%s)" % (t.val, self.tree2str(t.left))
#         else:
#             return "%s" % t.val

class Solution:

    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        result, stack, visited = '', [t], set()

        while stack:
            node = stack[-1]
            if node in visited:
                stack.pop()
                result += ')'
            else:
                visited.add(node)

                result += '(%d' % node.val

                if node.right and not node.left:
                    stack.append(node.right)
                    result += '()'

                if node.left:
                    stack.append(node.left)

        return result[1:-1]

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(7)
    root.left.right.left = TreeNode(10)
    # root.right.left = TreeNode(8)
    root.right.right = TreeNode(9)

    print(Solution().tree2str(root))