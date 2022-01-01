#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if char in node:
                node = node[char]
            else:
                node[char] = {}
                node = node[char]
        node['#'] = '#'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char in node:
                node = node[char]
            else:
                return False
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return False
        return True

if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("ple")
    assert not trie.search("app")
    assert trie.startsWith("app")
    assert not trie.startsWith("pp")
