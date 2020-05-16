#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:

    # class Trie:
    #     def __init__(self):
    #         self.root = {}
        
    #     def add(self, word: str):
    #         node = self.root
    #         for char in word:
    #             if char not in node:
    #                 node[char] = {}
    #             node = node[char]
    #         node['#'] = word
        
    #     def startswith(self, char: str, begin: {}) -> {}:
    #         node = begin if begin else self.root
    #         if char in node:
    #             return node[char]
        
    #     def remove(self, word: str):
    #         def _remove(node, depth: int):
    #             if len(word) == depth:
    #                 if self.is_word(node):
    #                     del node['#']
    #                 return
    #             char = word[depth]
    #             found = self.startswith(char, node)
    #             if found:
    #                 _remove(found, depth+1)
    #                 if len(found) == 0:
    #                     del node[char]
    #             else:
    #                 return

    #         _remove(self.root, 0)
        
    #     def is_empty(self, node) -> bool:
    #         return len(node) == 0 and not self.is_word(node)

    #     def is_word(self, node: {}) -> bool:
    #         return '#' in node if node else False

    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #     trie = Solution.Trie()
    #     for word in words:
    #         trie.add(word)
        
    #     ans = []
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             self.find_word(board, i, j, trie, set(), ans)
    #     return ans
    
    # def find_word(self, board, i, j, trie, visited, ans, node = None):
    #     char = board[i][j]
    #     position = trie.startswith(char, node)
    #     if position:
    #         visited.add((i, j))
    #         if trie.is_word(position):
    #             word = position['#']
    #             trie.remove(word)
    #             ans.append(word)
    #         test_positions = [
    #             (i - 1, j),
    #             (i + 1, j),
    #             (i, j - 1),
    #             (i, j + 1),
    #         ]
    #         for test_position in test_positions:
    #             if test_position in visited: continue
    #             if not (0 <= test_position[0] < len(board)): continue
    #             if not (0 <= test_position[1] < len(board[0])): continue
    #             self.find_word(board, test_position[0], test_position[1], trie, visited, ans, position)
    #         visited.remove((i, j))

    # 简洁版
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 初始化 trie
        WORD_KEY = '$'
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[WORD_KEY] = word
        
        # 回溯
        ans = []
        def backtracking(i, j, parent):
            char = board[i][j]
            node = parent[char]

            word = node.pop(WORD_KEY, None)
            if word: ans.append(word)
            
            board[i][j] = '#' # 不需要额外的空间记录访问过的 Cell
            for i_offset, j_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_i, new_j = i + i_offset, j + j_offset
                if not (0 <= new_i < len(board)): continue
                if not (0 <= new_j < len(board[0])): continue
                if board[new_i][new_j] not in node: continue
                backtracking(new_i, new_j, node)

            if not node: # 空节点
                del parent[char]

            board[i][j] = char
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    backtracking(i, j, trie)
        return ans

if __name__ == '__main__':
    ans = Solution().findWords([["o","a","a","n"],["e","t","a","e"],["r","h","k","r"],["r","f","l","v"]], ["oeo", "er", "oath","pea","eat","rain"])
    print(ans)
    ans = Solution().findWords([["a","a"]], ["a"])
    print(ans)